from typing import Generic, T, Any


class SingletonNotInitiatedError(Exception): ...


class Singleton(type, Generic[T]):
    __instances: dict = {}
    __slots__: tuple[str, ...] = ()

    def __call__(cls, *args: Any, **kwargs: Any) -> T:  # noqa: ANN401
        if cls not in cls.__instances:
            for key in cls.__slots__:
                if not key.startswith("__") and key.lstrip("_") not in kwargs:
                    raise SingletonNotInitiatedError(
                        f"Not initiated: key: {key}, class: {cls.__name__}, slots: {cls.__slots__}"
                    )
            cls.__instances[cls] = super().__call__(*args, **kwargs)

        return cls.__instances[cls]

    def clear_instance(cls) -> None:
        if cls in cls.__instances:
            cls.__instances[cls] = None
            del cls.__instances[cls]
