from typing import List


class ConiferTree:
    """
    Базовый класс, описывающий хвойное дерево.
    """

    def __init__(self, species: str, height: float, age: int) -> None:
        """
        Конструктор базового класса.

        Args:
            species (str): вид дерева
            height (float): высота дерева (м)
            age (int): возраст дерева (лет)
        """
        self.species: str = species
        self.height: float = height
        self.age: int = age

        # защищённый атрибут
        # хранит историю роста дерева
        self._growth_history: List[float] = []

        # приватный атрибут для внутренней идентификации
        self.__tree_id: int = id(self)

    def grow(self, meters: float) -> float:
        """
        Увеличивает высоту дерева.

        Args:
            meters (float): прирост высоты

        Returns:
            float: новая высота
        """
        self.height += meters
        self._growth_history.append(meters)
        return self.height

    def produce_cones(self) -> str:
        """
        Метод образования шишек.

        Returns:
            str: сообщение о появлении шишек
        """
        return "The tree produced cones."

    def __str__(self) -> str:
        return f"{self.species} tree, height: {self.height} m, age: {self.age} years"

    def __repr__(self) -> str:
        return (
            f"ConiferTree(species={self.species!r}, "
            f"height={self.height!r}, age={self.age!r})"
        )


class Spruce(ConiferTree):
    """
    Дочерний класс, представляющий ель.
    """

    def __init__(self, height: float, age: int, needle_length: float) -> None:
        """
        Конструктор класса Spruce.

        Args:
            height (float): высота
            age (int): возраст
            needle_length (float): длина хвои
        """
        super().__init__("Spruce", height, age)
        self.needle_length: float = needle_length

    def grow(self, meters: float) -> float:
        """
        Переопределение метода роста.

        Причина перегрузки:
        ели обычно растут немного медленнее из-за
        плотной кроны.

        Returns:
            float: новая высота
        """
        meters *= 0.9
        return super().grow(meters)

    def __str__(self) -> str:
        return f"Spruce tree, height {self.height} m, needle length {self.needle_length} cm"

    def __repr__(self) -> str:
        return (
            f"Spruce(height={self.height!r}, age={self.age!r}, "
            f"needle_length={self.needle_length!r})"
        )


class Pine(ConiferTree):
    """
    Дочерний класс, представляющий сосну.
    """

    def __init__(self, height: float, age: int, cone_size: float) -> None:
        super().__init__("Pine", height, age)
        self.cone_size: float = cone_size

    def grow(self, meters: float) -> float:
        """
        Переопределение метода роста.

        Причина перегрузки:
        сосны могут расти быстрее из-за более
        лёгкой структуры кроны.

        Returns:
            float: новая высота
        """
        meters *= 1.1
        return super().grow(meters)

    def __str__(self) -> str:
        return f"Pine tree, height {self.height} m, cone size {self.cone_size} cm"

    def __repr__(self) -> str:
        return (
            f"Pine(height={self.height!r}, age={self.age!r}, "
            f"cone_size={self.cone_size!r})"
        )


if __name__ == "__main__":
    spruce = Spruce(12.5, 8, 2.5)
    pine = Pine(15.0, 10, 6.0)

    print(spruce)
    print("New height:", spruce.grow(1.2))

    print()

    print(pine)
    print("New height:", pine.grow(1.2))