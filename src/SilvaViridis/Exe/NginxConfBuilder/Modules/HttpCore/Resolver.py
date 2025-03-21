from typing import Annotated, Sequence

from ._DirectivesList import DIR_RESOLVER
from ...Common import DirectiveBase, OnOff, Path, TimeInterval, TimeIntervalGroup
from ...Common.Validators import NonEmptySequenceValidator

AddressList = Annotated[Sequence[Path], NonEmptySequenceValidator]

class Resolver(DirectiveBase):
    def __init__(
        self,
        addresses : AddressList,
        valid : TimeInterval | TimeIntervalGroup | None = None,
        ipv4 : OnOff | None = None,
        ipv6 : OnOff | None = None,
        #TODO
    ):
        super().__init__(DIR_RESOLVER)

        for address in addresses:
            self.add_arg(address)

        self.add_arg(valid)
        self.add_arg(ipv4)
        self.add_arg(ipv6)
