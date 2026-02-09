import doctest
from typing import Optional, List


class Guitar:
    """
    Класс, представляющий гитару.
    """

    def __init__(self, brand: str, model: str, strings_count: int, body_type: str):
        """
        Создание и подготовка к работе объекта "Гитара"

        :param brand: Бренд гитары
        :param model: Модель гитары
        :param strings_count: Количество струн
        :param body_type: Тип корпуса

        Примеры:
        >>> guitar = Guitar("Fender", "Stratocaster", 6, "Solid Body")
        >>> guitar.brand
        'Fender'
        >>> guitar.strings_count
        6
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой")
        if len(brand.strip()) == 0:
            raise ValueError("Бренд не может быть пустой строкой")
        self.brand = brand.strip()

        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if len(model.strip()) == 0:
            raise ValueError("Модель не может быть пустой строкой")
        self.model = model.strip()

        if not isinstance(strings_count, int):
            raise TypeError("Количество струн должно быть целым числом")
        if strings_count not in [6, 7, 12]:
            raise ValueError("Количество струн должно быть 6, 7 или 12")
        self.strings_count = strings_count

        if not isinstance(body_type, str):
            raise TypeError("Тип корпуса должен быть строкой")
        if body_type not in ["Solid Body", "Hollow Body", "Semi-Hollow"]:
            raise ValueError("Неверный тип корпуса")
        self.body_type = body_type

        self._is_tuned = False
        self._volume_knob = 5

    def tune(self) -> None:
        """
        Настроить гитару.

        Примеры:
        >>> guitar = Guitar("Gibson", "Les Paul", 6, "Solid Body")
        >>> guitar.tune()
        """
        self._is_tuned = True

    def play_chord(self, chord: str) -> str:
        """
        Играть аккорд.

        :param chord: Название аккорда
        :return: Описание звучания

        Примеры:
        >>> guitar = Guitar("Ibanez", "RG550", 7, "Solid Body")
        >>> "звук" in guitar.play_chord("Am").lower()
        True
        """
        if not isinstance(chord, str):
            raise TypeError("Аккорд должен быть строкой")
        if len(chord.strip()) == 0:
            raise ValueError("Аккорд не может быть пустой строкой")

        # Заглушка для реализации
        ...
        if not self._is_tuned:
            return "Гитара не настроена!"
        return f"Звучит аккорд {chord}"

    def adjust_volume(self, level: int) -> int:
        """
        Регулировка громкости.

        :param level: Уровень громкости (0-10)
        :return: Текущий уровень громкости

        Примеры:
        >>> guitar = Guitar("PRS", "Custom 24", 6, "Solid Body")
        >>> 0 <= guitar.adjust_volume(7) <= 10
        True
        """
        if not isinstance(level, int):
            raise TypeError("Уровень громкости должен быть целым числом")
        if not (0 <= level <= 10):
            raise ValueError("Уровень громкости должен быть от 0 до 10")

        # Заглушка для реализации
        ...
        self._volume_knob = level
        return self._volume_knob


class Piano:
    """
    Класс, представляющий пианино.
    """

    def __init__(self, brand: str, keys_count: int, is_acoustic: bool):
        """
        Создание и подготовка к работе объекта "Пианино"

        :param brand: Бренд пианино
        :param keys_count: Количество клавиш
        :param is_acoustic: Акустическое ли пианино

        Примеры:
        >>> piano = Piano("Yamaha", 88, True)
        >>> piano.brand
        'Yamaha'
        >>> piano.keys_count
        88
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой")
        if len(brand.strip()) == 0:
            raise ValueError("Бренд не может быть пустой строкой")
        self.brand = brand.strip()

        if not isinstance(keys_count, int):
            raise TypeError("Количество клавиш должно быть целым числом")
        if keys_count not in [61, 76, 88]:
            raise ValueError("Количество клавиш должно быть 61, 76 или 88")
        self.keys_count = keys_count

        if not isinstance(is_acoustic, bool):
            raise TypeError("Тип пианино должен быть булевым значением")
        self.is_acoustic = is_acoustic

        self._is_open = False
        self._pedal_pressed = False

    def open_lid(self) -> None:
        """
        Открыть крышку пианино.

        Примеры:
        >>> piano = Piano("Kawai", 88, True)
        >>> piano.open_lid()
        """
        self._is_open = True

    def close_lid(self) -> None:
        """
        Закрыть крышку пианино.

        Примеры:
        >>> piano = Piano("Steinway", 88, True)
        >>> piano.open_lid()
        >>> piano.close_lid()
        """
        self._is_open = False

    def press_pedal(self) -> None:
        """
        Нажать педаль сустейна.

        Примеры:
        >>> piano = Piano("Casio", 88, False)
        >>> piano.press_pedal()
        """
        self._pedal_pressed = True

    def release_pedal(self) -> None:
        """
        Отпустить педаль.

        Примеры:
        >>> piano = Piano("Roland", 76, False)
        >>> piano.press_pedal()
        >>> piano.release_pedal()
        """
        self._pedal_pressed = False

    def play_note(self, note: str, duration: float) -> str:
        """
        Играть ноту.

        :param note: Название ноты (например, "C4")
        :param duration: Длительность в секундах
        :return: Описание звучания

        Примеры:
        >>> piano = Piano("Korg", 61, False)
        >>> "звучит" in piano.play_note("A4", 1.0).lower()
        True
        """
        if not isinstance(note, str):
            raise TypeError("Нота должна быть строкой")
        if len(note.strip()) == 0:
            raise ValueError("Нота не может быть пустой строкой")

        if not isinstance(duration, (int, float)):
            raise TypeError("Длительность должна быть числом")
        if duration <= 0:
            raise ValueError("Длительность должна быть положительным числом")

        # Заглушка для реализации
        ...
        sustain = "с педалью" if self._pedal_pressed else ""
        return f"Звучит нота {note} в течение {duration} секунд {sustain}"


class DrumSet:
    """
    Класс, представляющий барабанную установку.
    """

    def __init__(self, brand: str, pieces_count: int, material: str):
        """
        Создание и подготовка к работе объекта "Барабанная установка"

        :param brand: Бренд установки
        :param pieces_count: Количество барабанов
        :param material: Материал барабанов

        Примеры:
        >>> drums = DrumSet("Pearl", 5, "Maple")
        >>> drums.brand
        'Pearl'
        >>> drums.pieces_count
        5
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой")
        if len(brand.strip()) == 0:
            raise ValueError("Бренд не может быть пустой строкой")
        self.brand = brand.strip()

        if not isinstance(pieces_count, int):
            raise TypeError("Количество барабанов должно быть целым числом")
        if not (3 <= pieces_count <= 10):
            raise ValueError("Количество барабанов должно быть от 3 до 10")
        self.pieces_count = pieces_count

        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")
        if material not in ["Maple", "Birch", "Mahogany", "Poplar"]:
            raise ValueError("Неверный материал барабанов")
        self.material = material

        self._is_assembled = True
        self._tuning = "Стандартный строй"

    def assemble(self) -> None:
        """
        Собрать установку.

        Примеры:
        >>> drums = DrumSet("Tama", 6, "Birch")
        >>> drums.assemble()
        """
        self._is_assembled = True

    def disassemble(self) -> None:
        """
        Разобрать установку.

        Примеры:
        >>> drums = DrumSet("DW", 7, "Maple")
        >>> drums.assemble()
        >>> drums.disassemble()
        """
        self._is_assembled = False

    def tune_drums(self, tuning: str) -> str:
        """
        Настроить барабаны.

        :param tuning: Тип строя
        :return: Текущий строй

        Примеры:
        >>> drums = DrumSet("Yamaha", 5, "Mahogany")
        >>> drums.tune_drums("Низкий строй")
        'Низкий строй'
        """
        if not isinstance(tuning, str):
            raise TypeError("Строй должен быть строкой")
        if len(tuning.strip()) == 0:
            raise ValueError("Строй не может быть пустой строкой")

        # Заглушка для реализации
        ...
        self._tuning = tuning
        return self._tuning

    def play_beat(self, tempo: int) -> str:
        """
        Играть ритм.

        :param tempo: Темп в BPM (удары в минуту)
        :return: Описание ритма

        Примеры:
        >>> drums = DrumSet("Ludwig", 4, "Poplar")
        >>> "ритм" in drums.play_beat(120).lower()
        True
        """
        if not isinstance(tempo, int):
            raise TypeError("Темп должен быть целым числом")
        if not (40 <= tempo <= 220):
            raise ValueError("Темп должен быть в диапазоне 40-220 BPM")

        # Заглушка для реализации
        ...
        if tempo < 100:
            return f"Медленный ритм {tempo} BPM"
        elif tempo < 160:
            return f"Средний ритм {tempo} BPM"
        else:
            return f"Быстрый ритм {tempo} BPM"


if __name__ == "__main__":
    # Запуск doctest для проверки примеров в документации
    doctest.testmod(verbose=True)

    # Демонстрация работы классов
    print("\n" + "=" * 50)
    print("Вариант 2: Музыкальные инструменты")
    print("=" * 50)

    # 1. Гитара
    print("\n1. Класс Guitar:")
    guitar = Guitar("Fender", "Telecaster", 6, "Solid Body")
    print(f"   Создана: {guitar.brand} {guitar.model}")
    print(f"   Струн: {guitar.strings_count}")
    print(f"   Корпус: {guitar.body_type}")

    # 2. Пианино
    print("\n2. Класс Piano:")
    piano = Piano("Steinway & Sons", 88, True)
    print(f"   Создано: {piano.brand}")
    print(f"   Клавиш: {piano.keys_count}")
    print(f"   Акустическое: {'Да' if piano.is_acoustic else 'Нет'}")

    # 3. Барабанная установка
    print("\n3. Класс DrumSet:")
    drums = DrumSet("Pearl", 6, "Maple")
    print(f"   Создана: {drums.brand}")
    print(f"   Барабанов: {drums.pieces_count}")
    print(f"   Материал: {drums.material}")

    print("\n" + "=" * 50)
    print("Все музыкальные инструменты созданы успешно!")