% close open figures
close all
% known posts
post1 = [0, 4.7];
post2 = [0, 0];

% plot known posts with x
scatter([post1(1), post2(1)], [post1(2), post2(2)], 'x')
% don't erase on further graphing 
hold on

% set graphing limits
ylim([0, 4.7])
xlim([-7.38, 7.38])

while 1
    %get input from the mouse
    inputLocation = ginput(1);
    scatter(inputLocation(1), inputLocation(2), '*r')
    %find distances to mouse location
    topDistance = norm(inputLocation - post1);
    bottomDistance = norm(inputLocation - post2);
    % use location finding function
    location = findLocation(post2, topDistance, bottomDistance, abs(post1(2)-post2(2)));
    % plot found position with blue +
    scatter(location(1), location(2), '+b')
    legend('posts', 'real location', 'found location')
end