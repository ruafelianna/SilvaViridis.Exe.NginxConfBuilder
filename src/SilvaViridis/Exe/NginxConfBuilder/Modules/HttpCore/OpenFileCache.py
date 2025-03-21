from typing import Literal

from ._DirectivesList import DIR_OPEN_FILE_CACHE
from ...Common import DirectiveBase, OnOff, TimeInterval, TimeIntervalGroup
from ...Common.Validators import PositiveInt

class OpenFileCache(DirectiveBase):
    def __init__(
        self,
        state : Literal[OnOff.off] | PositiveInt = OnOff.off,
        inactive : TimeInterval | TimeIntervalGroup | None = None,
    ):
        super().__init__(DIR_OPEN_FILE_CACHE)

        if state == OnOff.off:
            self.add_arg(state)
        else:
            self.add_arg(state, "max=")
            self.add_arg(TimeInterval(60) if inactive is None else inactive)
