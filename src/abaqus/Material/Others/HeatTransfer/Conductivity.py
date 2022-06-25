from abaqusConstants import *


class Conductivity:
    r"""The Conductivity object specifies thermal conductivity.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import material
            mdb.models[name].materials[name].conductivity
            import odbMaterial
            session.odbs[name].materials[name].conductivity

        The table data for this object are:

        - If **type** = ISOTROPIC, the table data specify the following:
        
            - Conductivity, :math:`k`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = ORTHOTROPIC, the table data specify the following:
        
            - :math:`k_{11}`
            - :math:`k_{22}`.
            - :math:`k_{33}`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **type** = ANISOTROPIC, the table data specify the following:
        
            - :math:`k_{11}`.
            - :math:`k_{12}`.
            - :math:`k_{22}`.
            - :math:`k_{13}`.
            - :math:`k_{23}`.
            - :math:`k_{33}`.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        The corresponding analysis keywords are:

        - CONDUCTIVITY
    """

    def __init__(
        self,
        table: tuple,
        type: SymbolicConstant = ISOTROPIC,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
    ):
        """This method creates a Conductivity object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].materials[name].Conductivity
                session.odbs[name].materials[name].Conductivity

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        type
            A SymbolicConstant specifying the type of conductivity. Possible values are ISOTROPIC,
            ORTHOTROPIC, and ANISOTROPIC. The default value is ISOTROPIC.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.

        Returns
        -------
        Conductivity
            A :py:class:`~abaqus.Material.Others.HeatTransfer.Conductivity.Conductivity` object.

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self, *args, **kwargs):
        """This method modifies the Conductivity object.

        Raises
        ------
        RangeError
        """
        pass
