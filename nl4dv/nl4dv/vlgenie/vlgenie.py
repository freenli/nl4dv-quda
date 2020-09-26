from nl4dv.utils import constants


class VLGenie():

    def __init__(self):

        self.vl_spec = dict()
        self.vl_spec['$schema'] = 'https://vega.github.io/schema/vega-lite/v4.json'
        self.vl_spec['mark'] = dict()
        self.vl_spec['encoding'] = dict()
        self.vl_spec['transform'] = list()
        self.bin = False

        # Score object
        self.score_obj = {
            "by_attributes": 0,
            "by_task": 0,
            "by_vis": 0
        }

    def set_vis_type(self, vis):

        if vis == 'histogram':
            self.vl_spec['mark']['type'] = 'bar'
            self.bin = True

        elif vis == 'barchart':
            self.vl_spec['mark']['type'] = 'bar'

        elif vis == 'linechart':
            self.vl_spec['mark']['type'] = 'line'

        elif vis == 'areachart':
            self.vl_spec['mark']['type'] = 'area'

        elif vis == 'scatterplot':
            self.vl_spec['mark']['type'] = 'point'

        elif vis == 'boxplot':
            self.vl_spec['mark']['type'] = 'boxplot'

        elif vis == 'stripplot':
            self.vl_spec['mark']['type'] = 'tick'

        elif vis == 'piechart':
            self.vl_spec['mark']['type'] = 'arc'

        elif vis == 'donutchart':
            self.vl_spec['mark']['type'] = 'arc'
            self.vl_spec['mark']['innerRadius'] = 50

        elif vis == 'datatable':
            # Remove unneeded encodings
            del self.vl_spec['mark']
            del self.vl_spec['encoding']

            # Derive a new "row_number" variable with a sequence of numbers (used as index / counter later on)
            self.vl_spec["transform"] = [{
                "window": [{"op": "row_number", "as": "row_number"}]
            }]

            # Horizontally concatenate each attribute's column (VIS with mark type = text)
            self.vl_spec["hconcat"] = []

    def create_and_add_column_to_datatable(self, attr):

            # VL specification for a column of text. Use the row_number as the y_axis encoding to render vertically. Sly!
            column = {
                "width": 150,
                "title": attr,
                "mark": "text",
                "encoding": {
                    "text": {"field": attr, "type": "nominal"},
                    "y": {"field": "row_number", "type": "ordinal", "axis": None}
                }
            }
            self.vl_spec["hconcat"].append(column)

    def unset_encoding(self, dim):
        if dim in self.vl_spec['encoding']:
            del self.vl_spec['encoding'][dim]

    def get_encoding(self, dim):
        return self.vl_spec['encoding'][dim]

    def set_encoding_aggregate(self, dim, aggregate):
        self.vl_spec['encoding'][dim]['aggregate'] = aggregate

    def set_encoding(self, dim, attr, attr_type, aggregate=None):

        self.vl_spec['encoding'][dim] = dict()
        self.vl_spec['encoding'][dim]['field'] = attr
        self.vl_spec['encoding'][dim]['type'] = constants.vl_attribute_types[attr_type]
        self.vl_spec['encoding'][dim]['aggregate'] = aggregate

        if dim == 'x':
            if self.bin:
                self.vl_spec['encoding'][dim]['bin'] = True

    def set_task(self, dim, task, attr_list, key):
        if task["task"] == 'filter':
            if task["operator"] == 'IN':
                for attr in task['attributes']:
                    if key == False:
                        self.vl_spec['transform'].append({'filter': {"field": attr, "oneOf": task["values"]}})
                    elif key == True and 'color' in self.vl_spec['encoding']:
                        if 'condition' in self.vl_spec['encoding']['color']:
                            self.vl_spec['encoding']['color']['condition']['test']['and'].append(
                                {
                                    "field": attr,
                                    "oneOf": task["values"]
                                }
                            )
                        else:
                            self.vl_spec['transform'].append({'filter': {"field": attr, "oneOf": task["values"]}})
                    else:
                        self.vl_spec['encoding']['color'] = {
                            "condition": {
                                "test": {
                                    "and": [
                                        {
                                           "field": attr,
                                           "oneOf": task["values"]
                                        }
                                    ]
                                },
                                "value": "#c30d24"
                            },
                            "value": "#1770ab"
                        }
            elif task["operator"] == 'RANGE':
                for attr in task['attributes']:
                    self.vl_spec['transform'].append({"filter": {"field": attr, "range": task["values"]}})
            elif task["operator"] == 'NOT RANGE':
                for attr in task['attributes']:
                    self.vl_spec['transform'].append({"filter": {"not": {"field": attr, "range": task["values"]}}})
            else:
                for attr in task['attributes']:
                    symbol = constants.operator_symbol_mapping[task["operator"]]
                    self.vl_spec['transform'].append({'filter':'lower(datum["{}"]) {} {}'.format(attr, symbol, task["values"][0])})

    def set_data(self, dataUrl):
        # type: (list) -> None
        """
        Set domain data for the visualization

        """
        self.vl_spec['data'] = {'url': dataUrl, 'format': {'type': 'csv'}}

    def add_tick_format(self):
        for dim in self.vl_spec['encoding']:
            if dim in ['x','y'] and self.vl_spec['encoding'][dim]['type'] == 'quantitative':
                if 'axis' not in self.vl_spec['encoding'][dim]:
                    self.vl_spec['encoding'][dim]['axis'] = dict()
                self.vl_spec['encoding'][dim]['axis']["format"] = "s"

    def add_tooltip(self):
        self.vl_spec['mark']['tooltip'] = True
    
    def add_extent(self):
        self.vl_spec['mark']['extent'] = "min-max"

    def add_label_attribute_as_tooltip(self, label_attribute):
        # Check if any of the AXES (encodings) have existing aggregations. If not, then add tooltip which is the label
        has_aggregate = False
        for encoding in self.vl_spec['encoding']:
            if 'aggregate' in self.vl_spec['encoding'][encoding] and self.vl_spec['encoding'][encoding]['aggregate'] is not None:
                has_aggregate = True
                break

        if not has_aggregate:
            self.vl_spec['encoding']['tooltip'] = dict()
            self.vl_spec['encoding']['tooltip']["field"] = label_attribute
