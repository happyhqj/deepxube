from typing import Any

try:
    from torch.utils.tensorboard import SummaryWriter
except ModuleNotFoundError:
    class SummaryWriter:  # type: ignore[no-redef]
        def __init__(self, *_args: Any, **_kwargs: Any) -> None:
            print("tensorboard is not installed; training metrics will not be written.")

        def add_scalar(self, *_args: Any, **_kwargs: Any) -> None:
            pass

        def close(self) -> None:
            pass
