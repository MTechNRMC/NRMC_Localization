data = csvread(['D:\Obhi\Dropbox\NRMC\Locatization\Test Data\test4.csv']);

tol = 75; %tolerance value for +/- from the refernce point;
points = 5;

degrees = data(:,1)';
d = data(:,2)';
quality = data(:,3)';
deriv = diff(d);
deriv(deriv<0) = 0;
deriv_desc = sort(deriv,'descend');
deriv_desc = deriv_desc(find(deriv_desc));
% max number of sharp corners that will be considered, never below 2
% plot(degrees(1:length(deriv_desc)), deriv_desc);
degree_vector = zeros(1,points);
degree_indxs = zeros(1,points);
average_degrees = zeros(1,points);
average_distance = zeros(1,points);
% build the vector of angles that are suspected to have the targets
for i = 1:points
    ang_ind = find(deriv == deriv_desc(i));
    reference_value = min([d(ang_ind-1) d(ang_ind) d(ang_ind+1)]);
    distances_ind = find(d<reference_value+tol & d > reference_value-tol);
    average_degrees(i) = mean(degrees(distances_ind));
    average_distance(i) = mean( d(distances_ind) );
end
ind = find(average_distance == min(average_distance));
average_distance_ = average_distance(average_distance ~= min(average_distance));
ind2 = find(average_distance_ == min(average_distance_));
ind2_ = find(average_distance == average_distance_(ind2));
average_degrees = [average_degrees(ind) average_degrees(ind2_)];
average_distance = [average_distance(ind) average_distance(ind2_)];


phase_ = degrees*(pi/180);
[x, y] = pol2cart(phase_,d);
figure;
scatter(x,y)
figure;
polar(phase_,d)
figure;
deriv = diff(d);
hold on
plot(phase_*(180/pi),d);
plot(phase_(1:end-1)*(180/pi),deriv,'r');
hold off
