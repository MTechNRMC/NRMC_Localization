function location = findLocation(bottomPostLocation, topDistance,...
                                 bottomDistance, separation)
    location = ones(2);
    % find vertical offset (r1 is topDistance, r2 is bottomDistance
    % Circle equations: r2^2 = x^2 + y^2, r1^2 = x^2 + (y-separation)^2
    % Combine on second: r1^2 = (r2^2-y^2) + (y-separation)^2
    % Solve for y: y = (separation^2 + (r2^2-r1^2))/(2*separation)
    % Rearrange difference of squares:
    % y = ((r2-r1)*(r2+r1) + separation^2)/(2*separation)
    verticalOffset = ((bottomDistance-topDistance)*(bottomDistance+topDistance) + separation^2)/(2*separation);
    % find x given distance (hypoteneuse) and vertical offset
    location(1) = sqrt(bottomDistance^2 - verticalOffset^2);
    % find actual y given vertical offset
    location(2) = bottomPostLocation(2) + verticalOffset;
    disp(acos(verticalOffset/bottomDistance))
end