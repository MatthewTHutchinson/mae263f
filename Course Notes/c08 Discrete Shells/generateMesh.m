% Filename: generateMesh.m
% Demo of triangular mesh generation on a rectangular region
% Khalid Jawed (khalidjm@seas.ucla.edu)

l = 0.1; % length of the rectangle
w = 0.03; % width of the rectangle
maxMeshSize = w/5; % maximum size of the mesh
minMeshSize = maxMeshSize/2; % minimum size of the mesh

gd = [3; 4; 0; l; l; 0; 0; 0; w; w];
g = decsg(gd);
model = createpde;
geometryFromEdges(model,g); % create geometry (rectangle in our case)

FEMesh = generateMesh(model,'Hmax', maxMeshSize, 'Hmin', ...
    minMeshSize, 'GeometricOrder', 'linear'); % generate the mesh

% Extract the elements and nodes
Elements = FEMesh.Elements;
Nodes = FEMesh.Nodes;

% Plot
figure(2);
hold on
[~, numElements] = size(Elements);
for c=1:numElements
    node1_number = Elements(1,c);
    node2_number = Elements(2,c);
    node3_number = Elements(3,c);
    node1_position = Nodes(:, node1_number);
    node2_position = Nodes(:, node2_number);
    node3_position = Nodes(:, node3_number);
    
    x_arr = [node1_position(1), node2_position(1), node3_position(1), ...
        node1_position(1)];
    y_arr = [node1_position(2), node2_position(2), node3_position(2), ...
        node1_position(2)];
    plot( x_arr, y_arr, 'ro-');
end
hold off
axis equal
box on