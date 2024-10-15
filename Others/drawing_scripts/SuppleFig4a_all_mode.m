% Inputs

data = [ 89	4	6	17	1	0	0	0	0	0	0	0	0	0	0; ...
         0	71	0	0	0	0	0	0	0	0	0	0	0	0	0; ...
         23	38	386	0	9	0	0	0	0	0	0	0	0	0	0; ...
         0	0	0	0	0	0	0	0	0	0	0	0	0	0	0; ...
         6	0	0	3	48	0	0	0	0	0	0	0	0	0	0; ...
         0	9	4	2	362	419	0	0	0	0	0	0	0	0	0; ...
         0	0	0	0	0	0	0	0	0	0	0	0	0	0	0; ...
         0	0	0	0	0	0	0	0	0	0	0	0	0	0	0; ...
         0	0	0	0	0	0	0	0	38	0	0	0	0	2	0; ...
         0	0	0	0	0	0	0	0	0	0	0	0	0	0	0; ...
         0	0	0	0	0	0	0	0	0	0	0	0	0	0	0; ...
         0	0	0	0	0	0	0	0	0	0	0	1	0	0	0; ...
         0	0	0	0	0	0	0	0	0	0	0	0	0	0	0; ...
         0	0	0	0	0	0	0	0	0	0	0	0	0	0	0; ...
         0	0	0	0	0	0	0	0	0	0	0	0	0	0	0];



normalized_data = zeros(size(data));
for i = 1:size(data, 1)
    row = data(i, :);
    if sum(row) ~= 0
        normalized_row = row / sum(row);
    else
        normalized_row = row;
    end
    normalized_data(i, :) = normalized_row;
end


% disp(normalized_data);

rowWidths = repelem([5], 15);
colWidths = repelem([5], 15);

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
% cmap = [linspace(0.9216, .2431,  n)', linspace(0.949, .6549, n)', linspace(0.78039, .3529, n)'];

% disp(cmap);

% NBT purple cmap
% cmap = [linspace(0.99216, 0.470588,  n)', linspace(0.9686, 0.1294117, n)', linspace(0.90588, 0.584313, n)'];

% unify blue cmap
% cmap = [linspace(0.898039, 0.18431,  n)', linspace(0.93725, 0.470588, n)', linspace(0.941176, 0.709804, n)'];
 cmap = [linspace(0.898039, 0.40784,  n)', linspace(0.93725, 0.666666, n)', linspace(0.941176, 0.815686, n)'];
% cmap = [linspace(0.898039, 0.23529,  n)', linspace(0.93725, 0.537254, n)', linspace(0.941176, 0.745098, n)'];

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
colorbar('TickDirection', 'out');

axis tight
axis equal
view(2)

% Label X axis and Y axis
xlabel('Predict', 'FontSize', 18)
ylabel('Truth', 'FontSize', 18)


ax = gca;
ax.FontName = "Arial";
ax.XAxis.Label.Position(2) = -8.2;
ax.YAxis.Label.Position(1) = -11.2;


axis_mark = ["R9 G2" "R9 G4 FAST" "R9 G4 HAC" "R9 G6 FAST" "R9 G6 HAC" "R9 G6 SUP" "R9 D0 FAST" "R9 D0 HAC" "R9 D0 SUP" "R10 G6 FAST" "R10 G6 HAC" "R10 G6 SUP" "R10 D0 FAST" "R10 D0 HAC" "R10 D0 SUP"];

% find rectangle centers
xCnt = xg(1:end-1,1:end-1) + diff(xg(1,:))/2;
yCnt = yg(1:end-1,1:end-1) + diff(yg(:,1))/2;

% Add markers for X axis
for i = 1:size(xCnt, 2)
    text(xCnt(1,i)-2, yg(1,1)-4.5, axis_mark(i), ...
        'HorizontalAlignment','center',...
        'VerticalAlignment','middle', ...
        'FontSize', 18, 'Rotation', 45);
end

% Add markers for Y axis
for i = 1:size(yCnt, 1)
    text(xg(1,1)-6, yCnt(i,1), axis_mark(i), ...
        'HorizontalAlignment','center',...
        'VerticalAlignment','middle', ...
        'FontSize', 18);
end


% Add label to each grid
th = text(xCnt(:), yCnt(:), compose('%.2f', normalized_data(:)), ...
    'HorizontalAlignment','center',...
    'VerticalAlignment','middle', ...
    'FontSize', 18, 'Color', 'black');

% Remove X axis tick labels
xticks([]); 
yticks([]);






