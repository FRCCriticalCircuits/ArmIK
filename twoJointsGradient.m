function plot_error_surface()
    % 连杆长度
    y1 = 1;
    y2 = 1;
    % 目标位置
    Px = 1;
    Py = 2;
    
    % 生成 θ1 和 θ2 的网格，范围是正负 160 度
    theta_range = linspace(-160, 160, 100);  % 角度范围
    [Theta1, Theta2] = meshgrid(theta_range, theta_range);
    
    % 将角度转换为弧度进行计算
    Theta1_rad = deg2rad(Theta1);
    Theta2_rad = deg2rad(Theta2);
    
    % 计算误差
    Error = arrayfun(@(t1, t2) objective([t1, t2], Px, Py, y1, y2), Theta1_rad, Theta2_rad);
    
    % 绘制误差曲面图
    figure;
    surf(Theta1, Theta2, Error);
    xlabel('\theta_1 (degrees)');
    ylabel('\theta_2 (degrees)');
    zlabel('Error');
    title('Error Surface');
    colorbar;
end

function error = objective(angles, Px, Py, y1, y2)
    theta1 = angles(1);
    theta2 = angles(2);
    
    Px_estimate = -y1 * sin(theta1) - y2 * sin(theta1 + theta2);
    Py_estimate = y1 * cos(theta1) + y2 * cos(theta1 + theta2);
    
    error = sqrt((Px - Px_estimate)^2 + (Py - Py_estimate)^2);
end

plot_error_surface();
