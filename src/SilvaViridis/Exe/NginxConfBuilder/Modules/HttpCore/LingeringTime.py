from ._DirectivesList import DIR_LINGERING_TIME
from ...Common import DirectiveBase, TimeInterval, TimeIntervalGroup

class LingeringTime(DirectiveBase):
    def __init__(
        self,
        time : TimeInterval | TimeIntervalGroup = TimeInterval(30),
    ):
        super().__init__(DIR_LINGERING_TIME)
        self.add_arg(time)
