elif event.type == pygame.KEYDOWN:
    if event.key == pygame.K_1:
        if current_player == 1 and is_situation_selected:
            calculate_average_parameters()
            compute_total_error_and_declare_winner()
            current_player = 2  # Переключение на второго игрока
            is_situation_selected = False  # Сброс флага после расчета
    elif event.key == pygame.K_2:
        if current_player == 2 and is_situation_selected:
            calculate_average_parameters()
            compute_total_error_and_declare_winner()
            current_player = 1  # Сброс на первого игрока для новой игры
            is_situation_selected = False  # Сброс флага после расчета