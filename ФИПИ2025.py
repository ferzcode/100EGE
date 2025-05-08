import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# Проверяем доступные стили и выбираем подходящий
available_styles = plt.style.available
print("Доступные стили:", available_styles)
selected_style = 'seaborn-v0_8' if 'seaborn-v0_8' in available_styles else 'ggplot'
plt.style.use(selected_style)

# Создаем фигуру
plt.figure(figsize=(10, 10))
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title('Векторная диаграмма напряжений', pad=20)
plt.xlabel('Re, В')
plt.ylabel('Im, В')

# Масштабирование
scale = 1.2
plt.xlim(-25*scale, 40*scale)
plt.ylim(-25*scale, 25*scale)

# Данные векторов
vectors = {
    'U_R1': 8 * np.exp(1j * np.radians(90)),
    'U_L1': 8 * np.exp(1j * np.radians(180)),
    'U_C1': 16 * np.exp(1j * np.radians(0)),
    'U_L2': 34 * np.exp(1j * np.radians(45)),
    'U_C2': 22.64 * np.exp(1j * np.radians(-135)),
    'U_sum': 11.32 * np.exp(1j * np.radians(45))
}

# Цвета и стили
colors = ['red', 'green', 'blue', 'orange', 'purple', 'black']
linestyles = ['-', '-', '-', '-', '-', '--']

# Рисуем векторы
for i, (name, vec) in enumerate(vectors.items()):
    if i < len(vectors)-1:  # Основные векторы
        plt.quiver(0, 0, vec.real, vec.imag,
                  angles='xy', scale_units='xy', scale=1,
                  color=colors[i], width=0.005,
                  label=f'{name} = {abs(vec):.2f}e^j{np.degrees(np.angle(vec)):.0f}°')
    else:  # Суммарный вектор
        plt.quiver(0, 0, vec.real, vec.imag,
                  angles='xy', scale_units='xy', scale=1,
                  color=colors[i], width=0.005, linestyle=linestyles[i],
                  label=f'U_sum = {abs(vec):.2f}e^j{np.degrees(np.angle(vec)):.0f}°')

# Показываем сложение векторов для первой ветви
current = np.array([0, 0])
for vec in [vectors['U_R1'], vectors['U_L1'], vectors['U_C1']]:
    end = current + np.array([vec.real, vec.imag])
    plt.plot([current[0], end[0]], [current[1], end[1]],
             ':', color='gray', alpha=0.7)
    current = end

# Показываем сложение векторов для второй ветви
current = np.array([0, 0])
for vec in [vectors['U_L2'], vectors['U_C2']]:
    end = current + np.array([vec.real, vec.imag])
    plt.plot([current[0], end[0]], [current[1], end[1]],
             ':', color='gray', alpha=0.7)
    current = end

# Добавляем легенду
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Добавляем окружность для масштаба
circle = plt.Circle((0, 0), 11.32, color='gray', fill=False, linestyle=':', alpha=0.5)
plt.gca().add_patch(circle)
plt.text(11.32, 0, '11.32 В', ha='left', va='bottom')

plt.tight_layout()
plt.show()