import sys
from log_loader import load_logs
from log_filter import filter_logs_by_level
from log_counter import count_logs_by_level
from log_display import display_log_counts


def main():
    if len(sys.argv) < 2:
        print("Потрібно вказати шлях до файлу логів")
        return

    file_path = sys.argv[1]
    try:
        logs = load_logs(file_path)
    except FileNotFoundError:
        print("Файл логів не знайдено")
        return
    except Exception as e:
        print(f"Помилка при читанні файлу логів: {e}")
        return

    if len(sys.argv) >= 3:
        level_filter = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level_filter)
        display_log_counts(count_logs_by_level(logs))
        print(f"\nДеталі логів для рівня '{level_filter.upper()}':")
        for log in filtered_logs:
            print(f"{log['timestamp']} - {log['message']}")
    else:
        display_log_counts(count_logs_by_level(logs))

if __name__ == "__main__":
    main()