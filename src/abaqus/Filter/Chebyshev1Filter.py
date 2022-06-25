from abaqusConstants import *
from .Filter import Filter


class Chebyshev1Filter(Filter):
    """The Chebyshev1Filter object defines a Chebyshev type 1 filter.
    The Chebyshev1Filter object is derived from the Filter object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import filter
            mdb.models[name].filters[name]
            import odbFilter
            session.odbs[name].filters[name]

        The corresponding analysis keywords are:

        - FILTER
    """

    #: A String specifying the repository key. This name ANTIALIASING is reserved for filters
    #: generated internally by the program.
    name: str

    #: A Float specifying the attenuation point of the filter. Possible values are non-negative
    #: numbers. Order is not available for OperatorFilter.
    cutoffFrequency: float

    #: A Float specifying the amount of allowable ripple in the filter. Possible values are
    #: non-negative numbers. The default value is 0.225.
    rippleFactor: float = 0

    #: An Int specifying the highest power of the filter transfer function. Possible values are
    #: non-negative numbers less than or equal to 20. Order is not available for
    #: OperatorFilter. The default value is 2.
    order: int = 2

    #: A SymbolicConstant specifying the filter operator. Possible values are NONE, MIN, MAX,
    #: and ABS. The default value is NONE.
    operation: SymbolicConstant = NONE

    #: A Boolean specifying whether to stop the analysis if the specified limit is reached. The
    #: default value is OFF.
    halt: Boolean = OFF

    #: None or a Float specifying the threshold limit, an upper or lower bound for output
    #: values depending on the operation, or a bound for stopping the analysis when Halt is
    #: used. The default value is None.
    limit: float = None

    #: A SymbolicConstant specifying the invariant to which filtering is applied. Possible
    #: values are NONE, FIRST, and SECOND. The default value is NONE.
    invariant: SymbolicConstant = NONE

    def __init__(
        self,
        name: str,
        cutoffFrequency: float,
        rippleFactor: float = 0,
        order: int = 2,
        operation: SymbolicConstant = NONE,
        halt: Boolean = OFF,
        limit: float = None,
        invariant: SymbolicConstant = NONE,
    ):
        """This method creates a Chebyshev1Filter object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].Chebyshev1Filter
                session.odbs[name].Chebyshev1Filter

        Parameters
        ----------
        name
            A String specifying the repository key. This name ANTIALIASING is reserved for filters
            generated internally by the program.
        cutoffFrequency
            A Float specifying the attenuation point of the filter. Possible values are non-negative
            numbers. Order is not available for OperatorFilter.
        rippleFactor
            A Float specifying the amount of allowable ripple in the filter. Possible values are
            non-negative numbers. The default value is 0.225.
        order
            An Int specifying the highest power of the filter transfer function. Possible values are
            non-negative numbers less than or equal to 20. Order is not available for
            OperatorFilter. The default value is 2.
        operation
            A SymbolicConstant specifying the filter operator. Possible values are NONE, MIN, MAX,
            and ABS. The default value is NONE.
        halt
            A Boolean specifying whether to stop the analysis if the specified limit is reached. The
            default value is OFF.
        limit
            None or a Float specifying the threshold limit, an upper or lower bound for output
            values depending on the operation, or a bound for stopping the analysis when Halt is
            used. The default value is None.
        invariant
            A SymbolicConstant specifying the invariant to which filtering is applied. Possible
            values are NONE, FIRST, and SECOND. The default value is NONE.

        Returns
        -------
        Chebyshev1Filter
            A :py:class:`~abaqus.Filter.Chebyshev1Filter.Chebyshev1Filter` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        super().__init__()
        pass

    def setValues(
        self,
        rippleFactor: float = 0,
        order: int = 2,
        operation: SymbolicConstant = NONE,
        halt: Boolean = OFF,
        limit: float = None,
        invariant: SymbolicConstant = NONE,
    ):
        """This method modifies the Chebyshev1Filter object.

        Parameters
        ----------
        rippleFactor
            A Float specifying the amount of allowable ripple in the filter. Possible values are
            non-negative numbers. The default value is 0.225.
        order
            An Int specifying the highest power of the filter transfer function. Possible values are
            non-negative numbers less than or equal to 20. Order is not available for
            OperatorFilter. The default value is 2.
        operation
            A SymbolicConstant specifying the filter operator. Possible values are NONE, MIN, MAX,
            and ABS. The default value is NONE.
        halt
            A Boolean specifying whether to stop the analysis if the specified limit is reached. The
            default value is OFF.
        limit
            None or a Float specifying the threshold limit, an upper or lower bound for output
            values depending on the operation, or a bound for stopping the analysis when Halt is
            used. The default value is None.
        invariant
            A SymbolicConstant specifying the invariant to which filtering is applied. Possible
            values are NONE, FIRST, and SECOND. The default value is NONE.

        Raises
        ------
        RangeError
        """
        pass
