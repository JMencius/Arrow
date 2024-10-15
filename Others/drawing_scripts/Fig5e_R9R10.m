% Inputs
data = [ 385 4; ...
         0	60];

normalized_data = zeros(size(data));
for i = 1:size(data, 1)
    row = data(i, :);
    normalized_row = row / sum(row);
    normalized_data(i, :) = normalized_row;
end


% disp(normalized_data);

rowWidths = [45 30];
colWidths = [45 30];


%rowWidths = [10, 20];   %mm, one for each row of data; applied bottom to top
%colWidths = [5 15 20];  %mm, one for each col of data; applied left to right

% Produce figure
fig = figure(); 
ax = axes(fig); 

% Plot image
[xg,yg] = meshgrid([0,cumsum(colWidths)], [0,cumsum(rowWidths)]);
sh = surf(xg, yg, zeros(size(xg)), padarray(normalized_data,[1,1], 0, 'post'));

% Set colormap
n = 255;

% sky cmap
% cmap = [linspace(.9, 0, n)', linspace(.9447, .447, n)', linspace(.9741, .741, n)'];

% green cmap
% cmap = [linspace(0.9216, .2431,  n)', linspace(0.949, .6549, n)', linspace(0.9529, .3529, n)'];

% unify blue cmap
 cmap = [linspace(0.898039, 0.40784,  n)', linspace(0.93725, 0.666666, n)', linspace(0.941176, 0.815686, n)'];


disp(cmap);


%{
ano_cmap = [
            158 179 196
            182 194 160
            206 210 187
            230 226 181
            249 237 176
            243 218 152
            236 199 128
            231 179 106
            ];


normalized_cmap = zeros(size(ano_cmap));
for i = 1:size(ano_cmap, 1)
    row = ano_cmap(i, :);
    normalized_row = row / 255;
    normalized_cmap(i, :) = normalized_row;
end
%}

colormap(ax, cmap)
% cb = colorbar(ax, cmap);
colorbar('TickDirection', 'out');

axis tight
axis equal
view(2)

% Label X axis and Y axis
xlabel('Predict', 'FontSize', 18)
ylabel('Truth', 'FontSize', 18)


ax = gca;
ax.FontName = "Arial";
ax.XAxis.Label.Position(2) = -5.2;
ax.YAxis.Label.Position(1) = -6.2;


axis_mark = ["R9" "R10"];

% find rectangle centers
xCnt = xg(1:end-1,1:end-1) + diff(xg(1,:))/2;
yCnt = yg(1:end-1,1:end-1) + diff(yg(:,1))/2;

% Add markers for X axis
for i = 1:size(xCnt, 2)
    text(xCnt(1,i)-2, yg(1,1)-2.75, axis_mark(i), ...
        'HorizontalAlignment','center',...
        'VerticalAlignment','middle', ...
        'FontSize', 16, 'Rotation', 45);
end

% Add markers for Y axis
for i = 1:size(yCnt, 1)
    text(xg(1,1)-3.5, yCnt(i,1), axis_mark(i), ...
        'HorizontalAlignment','center',...
        'VerticalAlignment','middle', ...
        'FontSize', 16);
end


% Add label to each grid
th = text(xCnt(:), yCnt(:), compose('%.2f', normalized_data(:)), ...
    'HorizontalAlignment','center',...
    'VerticalAlignment','middle', ...
    'FontSize', 18, 'Color', 'black');

% Remove X axis tick labels
xticks([]); 
yticks([]);






