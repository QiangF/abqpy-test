from abaqusConstants import *
from .Interaction import Interaction
from ..Region.Region import Region


class FluidCavity(Interaction):
    """The FluidCavity object defines a surface-based cavity.
    The FluidCavity object is derived from the Interaction object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import interaction
            mdb.models[name].interactions[name]

        The corresponding analysis keywords are:

        - FLUID CAVITY
    """

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of the step in which the FluidCavity object is created.
    createStepName: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the fluid cavity reference point.
    cavityPoint: Region

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the surface forming the boundary of the fluid cavity.
    cavitySurface: Region

    #: A String specifying the FluidCavityProperty object associated with this interaction.
    interactionProperty: str

    #: A Float specifying the magnitude of the ambient pressure. The default value is 0.0.
    ambientPressure: float = 0

    #: A Float specifying the out-of-plane thickness of the surface for two-dimensional models.
    #: This argument is valid only when using two-dimensional models. The default value is 1.0.
    thickness: float = 1

    #: A Boolean specifying whether adiabatic behavior is assumed for the ideal gas. This
    #: argument is valid only when **interactionProperty** specifies a pneumatic definition. The
    #: default value is OFF.
    useAdiabatic: Boolean = OFF

    #: A Boolean specifying whether the analysis will check the consistency of the surface
    #: normals. The default value is ON.
    checkNormals: Boolean = ON

    def __init__(
        self,
        name: str,
        createStepName: str,
        cavityPoint: Region,
        cavitySurface: Region,
        interactionProperty: str,
        ambientPressure: float = 0,
        thickness: float = 1,
        useAdiabatic: Boolean = OFF,
        checkNormals: Boolean = ON,
    ):
        """This method creates an FluidCavity object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].FluidCavity

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A String specifying the name of the step in which the FluidCavity object is created.
        cavityPoint
            A :py:class:`~abaqus.Region.Region.Region` object specifying the fluid cavity reference point.
        cavitySurface
            A :py:class:`~abaqus.Region.Region.Region` object specifying the surface forming the boundary of the fluid cavity.
        interactionProperty
            A String specifying the FluidCavityProperty object associated with this interaction.
        ambientPressure
            A Float specifying the magnitude of the ambient pressure. The default value is 0.0.
        thickness
            A Float specifying the out-of-plane thickness of the surface for two-dimensional models.
            This argument is valid only when using two-dimensional models. The default value is 1.0.
        useAdiabatic
            A Boolean specifying whether adiabatic behavior is assumed for the ideal gas. This
            argument is valid only when **interactionProperty** specifies a pneumatic definition. The
            default value is OFF.
        checkNormals
            A Boolean specifying whether the analysis will check the consistency of the surface
            normals. The default value is ON.

        Returns
        -------
        FluidCavity
            A :py:class:`~abaqus.Interaction.FluidCavity.FluidCavity` object.
        """
        super().__init__()
        pass

    def setValues(
        self,
        ambientPressure: float = 0,
        thickness: float = 1,
        useAdiabatic: Boolean = OFF,
        checkNormals: Boolean = ON,
    ):
        """This method modifies the FluidCavity object.

        Parameters
        ----------
        ambientPressure
            A Float specifying the magnitude of the ambient pressure. The default value is 0.0.
        thickness
            A Float specifying the out-of-plane thickness of the surface for two-dimensional models.
            This argument is valid only when using two-dimensional models. The default value is 1.0.
        useAdiabatic
            A Boolean specifying whether adiabatic behavior is assumed for the ideal gas. This
            argument is valid only when **interactionProperty** specifies a pneumatic definition. The
            default value is OFF.
        checkNormals
            A Boolean specifying whether the analysis will check the consistency of the surface
            normals. The default value is ON.
        """
        pass
