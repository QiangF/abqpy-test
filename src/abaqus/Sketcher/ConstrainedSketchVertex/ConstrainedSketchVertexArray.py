import typing

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .ConstrainedSketchVertex import ConstrainedSketchVertex
from ...UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class ConstrainedSketchVertexArray(typing.List[ConstrainedSketchVertex]):
    """The ConstrainedSketchVertexArray is a sequence of ConstrainedSketchVertex objects.

    .. note:: 
        This object can be accessed by::

            import sketch
            mdb.models[name].sketches[name].vertices[i]
    """

    @abaqus_method_doc
    def findAt(self, coordinates: tuple, printWarning: Boolean = True) -> typing.Union[ConstrainedSketchVertex, typing.List[ConstrainedSketchVertex]]:
        """This method returns the ConstrainedSketchVertex located at the given coordinates.

        Parameters
        ----------
        coordinates
            A sequence of Floats specifying the **X**- and **Y**-coordinates of the object to find.
        printWarning
            A Boolean specifying whether a message is to be printed to the CLI if no entity is found
            at the specified location. The default value is True.

        Returns
        -------
        ConstrainedSketchVertex
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertex.ConstrainedSketchVertex` object.
        """
        return ConstrainedSketchVertex()
