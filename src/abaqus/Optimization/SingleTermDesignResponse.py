from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .DesignResponse import DesignResponse
from .StepOptionArray import StepOptionArray
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class SingleTermDesignResponse(DesignResponse):
    """The SingleTermDesignResponse object defines a single-term design response.
    The SingleTermDesignResponse object is derived from the DesignResponse object.

    .. note:: 
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name].designResponses[name]
    """

    #: A String specifying the design response repository key.
    name: str

    #: A String specifying the name of the variable identifier.
    identifier: str

    #: None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
    #: global coordinate system is used. When this member is queried, it returns an Int. The
    #: default value is None.
    csys: int = None

    #: None or a sequence of Floats specifying the driving region used when **identifier** is an
    #: internal nodal variable. The default value is None.
    drivingRegion: str = None

    #: A SymbolicConstant specifying the operation used on values in the region. Possible
    #: values are MAXIMUM, MINIMUM, and SUM. The default value is SUM.
    operation: SymbolicConstant = SUM

    #: The SymbolicConstant MODEL or a Region object specifying the region of the design
    #: response variable. The default value is MODEL.
    region: SymbolicConstant = MODEL

    #: A SymbolicConstant specifying the location used for shell layer values. Possible values
    #: are BOTTOM, MAXIMUM, MIDDLE, MINIMUM, and TOP. The default value is MAXIMUM.
    shellLayer: SymbolicConstant = MAXIMUM

    #: A SymbolicConstant specifying the operation used on values across steps and load cases.
    #: Possible values are MAXIMUM, MINIMUM, and SUM. The default value is SUM.
    stepOperation: SymbolicConstant = SUM

    #: A :py:class:`~abaqus.Optimization.StepOptionArray.StepOptionArray` object.
    stepOptions: StepOptionArray = None

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        identifier: str,
        csys: int = None,
        drivingRegion: str = None,
        operation: SymbolicConstant = SUM,
        region: SymbolicConstant = MODEL,
        shellLayer: SymbolicConstant = MAXIMUM,
        stepOperation: SymbolicConstant = SUM,
        stepOptions: StepOptionArray = None,
    ):
        """This method creates a SingleTermDesignResponse object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].SingleTermDesignResponse

        Parameters
        ----------
        name
            A String specifying the design response repository key.
        identifier
            A String specifying the name of the variable identifier.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        drivingRegion
            None or a sequence of Floats specifying the driving region used when **identifier** is an
            internal nodal variable. The default value is None.
        operation
            A SymbolicConstant specifying the operation used on values in the region. Possible
            values are MAXIMUM, MINIMUM, and SUM. The default value is SUM.
        region
            The SymbolicConstant MODEL or a Region object specifying the region of the design
            response variable. The default value is MODEL.
        shellLayer
            A SymbolicConstant specifying the location used for shell layer values. Possible values
            are BOTTOM, MAXIMUM, MIDDLE, MINIMUM, and TOP. The default value is MAXIMUM.
        stepOperation
            A SymbolicConstant specifying the operation used on values across steps and load cases.
            Possible values are MAXIMUM, MINIMUM, and SUM. The default value is SUM.
        stepOptions
            A :py:class:`~abaqus.Optimization.StepOptionArray.StepOptionArray` object.

        Returns
        -------
        SingleTermDesignResponse
            A :py:class:`~abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        csys: int = None,
        drivingRegion: str = None,
        operation: SymbolicConstant = SUM,
        region: SymbolicConstant = MODEL,
        shellLayer: SymbolicConstant = MAXIMUM,
        stepOperation: SymbolicConstant = SUM,
        stepOptions: StepOptionArray = None,
    ):
        """This method modifies the SingleTermDesignResponse object.

        Parameters
        ----------
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        drivingRegion
            None or a sequence of Floats specifying the driving region used when **identifier** is an
            internal nodal variable. The default value is None.
        operation
            A SymbolicConstant specifying the operation used on values in the region. Possible
            values are MAXIMUM, MINIMUM, and SUM. The default value is SUM.
        region
            The SymbolicConstant MODEL or a Region object specifying the region of the design
            response variable. The default value is MODEL.
        shellLayer
            A SymbolicConstant specifying the location used for shell layer values. Possible values
            are BOTTOM, MAXIMUM, MIDDLE, MINIMUM, and TOP. The default value is MAXIMUM.
        stepOperation
            A SymbolicConstant specifying the operation used on values across steps and load cases.
            Possible values are MAXIMUM, MINIMUM, and SUM. The default value is SUM.
        stepOptions
            A :py:class:`~abaqus.Optimization.StepOptionArray.StepOptionArray` object.
        """
        ...
