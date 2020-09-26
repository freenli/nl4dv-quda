vis_design_combos = {
    'Q': {
        'combination': 'Q',
        'support': True,
        'tasks': ['retrieve_value', 'filter', 'determine_range', 'distribution', 'find_extremum', 'find_anomalies'],
        'visualizations': ['histogram', 'stripplot', 'boxplot'],
        'designs': [{
            'task': 'retrieve_value',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x'],
            'priority': ['x'],
            'x': {'is_defined': False, 'agg': None}
        }, {
            'task': 'filter',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x'],
            'priority': ['x'],
            'x': {'is_defined': False, 'agg': None}
       }, {
           'task': 'determine_range',
           'vis_type': 'boxplot',
           'not_suggested_by_default': False,
           'mark': 'boxplot',
           'mandatory': ['x'],
           'priority': ['x'],
           'x': {'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'histogram',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y'],
            'priority': ['x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x'],
            'priority': ['x'],
            'x': {'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'boxplot',
            'not_suggested_by_default': True,
            'mark': 'boxplot',
            'mandatory': ['x'],
            'priority': ['x'],
            'x': {'is_defined': False, 'agg': None}
        }, {
            'task': 'find_extremum',
            'vis_type': 'boxplot',
            'not_suggested_by_default': False,
            'mark': 'boxplot',
            'mandatory': ['x'],
            'priority': ['x'],
            'x': {'is_defined': False, 'agg': None}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'boxplot',
            'not_suggested_by_default': False,
            'mark': 'boxplot',
            'mandatory': ['x'],
            'priority': ['x'],
            'x': {'is_defined': False, 'agg': None}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x'],
            'priority': ['x'],
            'x': {'is_defined': False, 'agg': None}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'histogram',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y'],
            'priority': ['x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'}
        }]
    },
    'N': {
        'combination': 'N',
        'support': True,
        'tasks': ['retrieve_value', 'filter', 'determine_range', 'distribution', 'derived_value'],
        'visualizations': ['stripplot', 'barchart'],
        'designs': [{
            'task': 'retrieve_value',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x'],
            'priority': ['x'],
            'x': {'is_defined': False, 'agg': None}
        }, {
            'task': 'filter',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y'],
            'priority': ['x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'}
        }, {
            'task': 'determine_range',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['y'],
            'priority': ['y'],
            'y': {'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y'],
            'priority': ['x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'}
        }, {
            'task': 'derived_value',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y'],
            'priority': ['x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'}
        }]
    },
    'O': {
        'combination': 'O',
        'support': True,
        'tasks': ['retrieve_value', 'filter', 'determine_range', 'distribution', 'derived_value'],
        'visualizations': ['stripplot', 'barchart'],
        'designs': [{
            'task': 'retrieve_value',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x'],
            'priority': ['x'],
            'x': {'is_defined': False, 'agg': None}
        }, {
            'task': 'filter',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y'],
            'priority': ['x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'}
        }, {
            'task': 'determine_range',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x'],
            'priority': ['x'],
            'x': {'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y'],
            'priority': ['x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'}
        }, {
            'task': 'derived_value',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y'],
            'priority': ['x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'}
        }]
    },
    'T': {
        'combination': 'T',
        'support': True,
        'tasks': ['retrieve_value', 'filter', 'determine_range','trend'],
        'visualizations': ['stripplot', 'linechart'],
        'designs': [{
            'task': 'retrieve_value',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x'],
            'priority': ['x'],
            'x': {'is_defined': False, 'agg': None}
        }, {
            'task': 'filter',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x'],
            'priority': ['x'],
            'x': {'is_defined': False, 'agg': None}
        }, {
            'task': 'determine_range',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x'],
            'priority': ['x'],
            'x': {'is_defined': False, 'agg': None}
        }, {
            'task': 'trend',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y'],
            'priority': ['x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'}
        }]
    },
    'QQ': {
        'combination': 'QQ',
        'support': True,
        'tasks': ['find_anomalies', 'correlation'],
        'visualizations': ['scatterplot'],
        'designs': [{
            'task': 'correlation',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y'],
            'priority': ['x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y'],
            'priority': ['x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None}
        }]
    },
    'QN': {
        'combination': 'QN',
        'support': True,
        'tasks': ['retrieve_value', 'filter', 'derived_value', 'find_extremum', 'sort', 'distribution', 'find_anomalies', 'cluster'],
        'visualizations': ['barchart', 'piechart', 'tickplot'],
        'designs': [{
            'task': 'derived_value',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y'],
            'priority': ['y', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'}
        }, {
            'task': 'derived_value',
            'vis_type': 'piechart',
            'not_suggested_by_default': True,
            'mark': 'arc',
            'mandatory': ['theta', 'color'],
            'priority': ['theta', 'color'],
            'color': {'attr': None, 'is_defined': False, 'agg': None},
            'theta': {'attr': None, 'is_defined': False, 'agg': 'mean'}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y'],
            'priority': ['y', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'retrieve_value',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y'],
            'priority': ['y', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'}
        }, {
            'task': 'retrieve_value',
            'vis_type': 'piechart',
            'not_suggested_by_default': True,
            'mark': 'arc',
            'mandatory': ['theta', 'color'],
            'priority': ['theta', 'color'],
            'color': {'attr': None, 'is_defined': False, 'agg': None},
            'theta': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'filter',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y'],
            'priority': ['y', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'filter',
            'vis_type': 'piechart',
            'not_suggested_by_default': True,
            'mark': 'arc',
            'mandatory': ['theta', 'color'],
            'priority': ['theta', 'color'],
            'color': {'attr': None, 'is_defined': False, 'agg': None},
            'theta': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
           'task': 'find_extremum',
           'vis_type': 'boxplot',
           'not_suggested_by_default': False,
           'mark': 'boxplot',
           'mandatory': ['x', 'y'],
           'priority': ['x', 'y'],
           'x': {'is_defined': False, 'agg': None, "scale": {"zero": False}},
           'y': {'is_defined': False, 'agg': None}
        }, {
            'task': 'sort',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y'],
            'priority': ['y', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'sort',
            'vis_type': 'piechart',
            'not_suggested_by_default': True,
            'mark': 'arc',
            'mandatory': ['theta', 'color'],
            'priority': ['theta', 'color'],
            'color': {'attr': None, 'is_defined': False, 'agg': None},
            'theta': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y'],
            'priority': ['y', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'piechart',
            'not_suggested_by_default': True,
            'mark': 'arc',
            'mandatory': ['theta', 'color'],
            'priority': ['theta', 'color'],
            'color': {'attr': None, 'is_defined': False, 'agg': None},
            'theta': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'cluster',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y'],
            'priority': ['y', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'cluster',
            'vis_type': 'piechart',
            'not_suggested_by_default': True,
            'mark': 'arc',
            'mandatory': ['theta', 'color'],
            'priority': ['theta', 'color'],
            'color': {'attr': None, 'is_defined': False, 'agg': None},
            'theta': {'attr': None, 'is_defined': False, 'agg': None}
        }]
    },
    'QO': {
        'combination': 'QO',
        'support': True,
        'tasks' : ['retrieve_value', 'filter', 'derived_value', 'find_extremum', 'sort', 'distribution', 'find_anomalies', 'cluster'],
        'visualizations': ['barchart', 'piechart', 'tickplot'],
        'designs': [{
            'task': 'derived_value',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y'],
            'priority': ['y', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'}
        }, {
            'task': 'derived_value',
            'vis_type': 'piechart',
            'not_suggested_by_default': True,
            'mark': 'arc',
            'mandatory': ['theta', 'color'],
            'priority': ['theta', 'color'],
            'color': {'attr': None, 'is_defined': False, 'agg': None},
            'theta': {'attr': None, 'is_defined': False, 'agg': 'mean'}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': True,
            'mark': 'tick',
            'mandatory': ['x', 'y'],
            'priority': ['y', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'retrieve_value',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y'],
            'priority': ['y', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'retrieve_value',
            'vis_type': 'piechart',
            'not_suggested_by_default': True,
            'mark': 'arc',
            'mandatory': ['theta', 'color'],
            'priority': ['theta', 'color'],
            'color': {'attr': None, 'is_defined': False, 'agg': None},
            'theta': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'filter',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y'],
            'priority': ['y', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'filter',
            'vis_type': 'piechart',
            'not_suggested_by_default': True,
            'mark': 'arc',
            'mandatory': ['theta', 'color'],
            'priority': ['theta', 'color'],
            'color': {'attr': None, 'is_defined': False, 'agg': None},
            'theta': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
           'task': 'find_extremum',
           'vis_type': 'boxplot',
           'not_suggested_by_default': False,
           'mark': 'boxplot',
           'mandatory': ['x', 'y'],
           'priority': ['x', 'y'],
           'x': {'is_defined': False, 'agg': None, "scale": {"zero": False}},
           'y': {'is_defined': False, 'agg': None}
        }, {
            'task': 'sort',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y'],
            'priority': ['y', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'sort',
            'vis_type': 'piechart',
            'not_suggested_by_default': False,
            'mark': 'arc',
            'mandatory': ['theta', 'color'],
            'priority': ['theta', 'color'],
            'color': {'attr': None, 'is_defined': False, 'agg': None},
            'theta': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y'],
            'priority': ['y', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'piechart',
            'not_suggested_by_default': True,
            'mark': 'arc',
            'mandatory': ['theta', 'color'],
            'priority': ['theta', 'color'],
            'color': {'attr': None, 'is_defined': False, 'agg': None},
            'theta': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'cluster',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y'],
            'priority': ['y', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'cluster',
            'vis_type': 'piechart',
            'not_suggested_by_default': True,
            'mark': 'arc',
            'mandatory': ['theta', 'color'],
            'priority': ['theta', 'color'],
            'color': {'attr': None, 'is_defined': False, 'agg': None},
            'theta': {'attr': None, 'is_defined': False, 'agg': None}
        }]
    },
    'QT': {
        'combination': 'QT',
        'support': True,
        'tasks' : ['distribution', 'find_anomalies', 'correlation', 'trend'],
        'visualizations': ['linechart', 'stripplot'],
        'designs': [{
            'task': 'trend',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y'],
            'priority': ['y', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y'],
            'priority': ['y', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y'],
            'priority': ['y', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'}
        }, {
            'task': 'correlation',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y'],
            'priority': ['y', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'correlation',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y'],
            'priority': ['y', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y'],
            'priority': ['y', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y'],
            'priority': ['y', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None}
        },]
    },
    'NN': {
        'combination': 'NN',
        'support': True,
        'tasks' : ['retrieve_value', 'filter', 'distribution', 'find_anomalies', 'cluster'],
        'visualizations': ['scatterplot', 'barchart'],
        'designs': [{
            'task': 'distribution',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'}
        }, {
            'task': 'distribution',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'retrieve_value',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y'],
            'priority': ['x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
        }, {
            'task': 'filter',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y'],
            'priority': ['x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
        }, {
            'task': 'find_anomalies',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y'],
            'priority': ['x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
        }, {
            'task': 'cluster',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y'],
            'priority': ['x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
        }]
    },
    'NO': {
        'combination': 'NO',
        'support': True,
        'tasks' : ['retrieve_value', 'filter', 'distribution', 'find_anomalies', 'cluster'],
        'visualizations': ['scatterplot', 'barchart'],
        'designs': [{
            'task': 'distribution',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'}
        }, {
            'task': 'distribution',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'retrieve_value',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y'],
            'priority': ['x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
        }, {
            'task': 'filter',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y'],
            'priority': ['x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
        }, {
            'task': 'find_anomalies',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y'],
            'priority': ['x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
        }, {
            'task': 'cluster',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y'],
            'priority': ['x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
        }]
    },
    'NT': {
        'combination': 'NT',
        'support': True,
        'tasks': ['trend', 'distribution'],
        'visualizations': ['linechart', 'stripplot'],
        'designs': [{
            'task': 'trend',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'trend',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }]
    },
    'OO': {
        'combination': 'OO',
        'support': True,
        'tasks' : ['retrieve_value', 'filter', 'distribution', 'find_anomalies', 'cluster'],
        'visualizations': ['scatterplot', 'barchart'],
        'designs': [{
            'task': 'distribution',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'}
        }, {
            'task': 'distribution',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'retrieve_value',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y'],
            'priority': ['x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
        }, {
            'task': 'filter',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y'],
            'priority': ['x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
        }, {
            'task': 'find_anomalies',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y'],
            'priority': ['x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
        }, {
            'task': 'cluster',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y'],
            'priority': ['x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
        }]
    },
    'OT': {
        'combination': 'OT',
        'support': True,
        'tasks': ['trend', 'distribution'],
        'visualizations': ['linechart', 'stripplot'],
        'designs': [{
            'task': 'trend',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'trend',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }]
    },
    'TT': {
        'combination': 'TT',
        'support': False,
        'tasks': [],
        'visualizations': [],
        'designs': []
    },
    'QQQ': {
        'combination': 'QQQ',
        'support': True,
        'tasks': ['find_anomalies', 'correlation'],
        'visualizations': ['scatterplot'],
        'designs': [{
            'task': 'correlation',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['x', 'y', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'correlation',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['x', 'y', 'size'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'scatterplot',
            'not_suggest_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['x', 'y', 'size'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['x', 'y', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }]
    },
    'QQN': {
        'combination': 'QQN',
        'support': True,
        'tasks' : ['retrieve_value', 'filter', 'find_extremum', 'sort', 'distribution', 'cluster', 'find_anomalies', 'correlation'],
        'visualizations': ['scatterplot', 'stripplot'],
        'designs': [{
            'task': 'correlation',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['x', 'y', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'correlation',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['x', 'y', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'retrieve_value',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'filter',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
           'task': 'find_extremum',
           'vis_type': 'boxplot',
           'not_suggested_by_default': False,
           'mark': 'boxplot',
           'mandatory': ['x', 'y', 'color'],
           'priority': ['x', 'color', 'y'],
           'x': {'is_defined': False, 'agg': None, "scale": {"zero": False}},
           'y': {'is_defined': False, 'agg': None},
           'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'sort',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'cluster',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['x', 'y', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['x', 'y', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }]
    },
    'QQO': {
        'combination': 'QQO',
        'support': True,
        'tasks' : ['retrieve_value', 'filter', 'find_extremum', 'sort', 'distribution', 'cluster', 'find_anomalies', 'correlation'],
        'visualizations': ['scatterplot', 'stripplot'],
        'designs': [{
            'task': 'correlation',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['x', 'y', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'correlation',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['x', 'y', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'retrieve_value',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'filter',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
           'task': 'find_extremum',
           'vis_type': 'boxplot',
           'not_suggested_by_default': False,
           'mark': 'boxplot',
           'mandatory': ['x', 'y', 'color'],
           'priority': ['x', 'color', 'y'],
           'x': {'is_defined': False, 'agg': None, "scale": {"zero": False}},
           'y': {'is_defined': False, 'agg': None},
           'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'sort',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'cluster',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['x', 'y', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['x', 'y', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }]
    },
    'QQT': {
        'combination': 'QQT',
        'support': True,
        'tasks' : ['distribution', 'find_anomalies', 'correlation'],
        'visualizations': ['scatterplot'],
        'designs': [{
            'task': 'correlation',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['x', 'y', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'correlation',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['x', 'y', 'size'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['color', 'y', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['size', 'y', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['x', 'y', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['x', 'y', 'size'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': None}
        }]
    },
    'QNN': {
        'combination': 'QNN',
        'support': True,
        'tasks' : ['retrieve_value', 'filter', 'derived_value', 'find_extremum', 'sort', 'distribution', 'find_anomalies', 'cluster'],
        'visualizations': ['barchart', 'scatterplot', 'stripplot'],
        'designs': [{
            'task': 'derived_value',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'sum'},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'derived_value',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'derived_value',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['size', 'x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': 'mean'}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'x', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['y', 'x', 'size'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'retrieve_value',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'retrieve_value',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'retrieve_value',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['size', 'x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'filter',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'filter',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'filter',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['size', 'x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
           'task': 'find_extremum',
           'vis_type': 'boxplot',
           'not_suggested_by_default': False,
           'mark': 'boxplot',
           'mandatory': ['x', 'y', 'color'],
           'priority': ['x', 'y', 'color'],
           'x': {'is_defined': False, 'agg': None, "scale": {"zero": False}},
           'y': {'is_defined': False, 'agg': None},
           'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'find_extremum',
            'vis_type': 'boxplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['x', 'y', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None, "scale": {"zero": False}},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'sort',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'sort',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['size', 'x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'cluster',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'cluster',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'cluster',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['size', 'x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': None}
        }]
    },
    'QNO': {
        'combination': 'QNO',
        'support': True,
        'tasks' : ['retrieve_value', 'filter', 'derived_value', 'find_extremum', 'sort', 'distribution', 'find_anomalies', 'cluster'],
        'visualizations': ['barchart', 'scatterplot', 'stripplot'],
        'designs': [{
            'task': 'derived_value',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'sum'},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'derived_value',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'derived_value',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['size', 'x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': 'mean'}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'x', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['y', 'x', 'size'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'retrieve_value',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'retrieve_value',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'retrieve_value',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['size', 'x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'filter',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'filter',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'filter',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['size', 'x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
           'task': 'find_extremum',
           'vis_type': 'boxplot',
           'not_suggested_by_default': False,
           'mark': 'boxplot',
           'mandatory': ['x', 'y', 'color'],
           'priority': ['x', 'y', 'color'],
           'x': {'is_defined': False, 'agg': None, "scale": {"zero": False}},
           'y': {'is_defined': False, 'agg': None},
           'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'find_extremum',
            'vis_type': 'boxplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['x', 'y', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None, "scale": {"zero": False}},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'sort',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'sort',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['size', 'x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'cluster',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'cluster',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'cluster',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['size', 'x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': None}
        }]
    },
    'QNT': {
        'combination': 'QNT',
        'support': True,
        'tasks' : ['distribution', 'trend'],
        #'tasks' : ['retrieve_value', 'filter', 'find_extremum', 'sort', 'distribution', 'find_anomalies', 'cluster', 'correlation', 'trend'],
        'visualizations': ['linechart', 'barchart', 'stripplot'],
        'designs': [{
            'task': 'trend',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'trend',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'trend',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'x', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'x', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': None}
        },{
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'x', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': None}
        }]
    },
    'QOO': {
        'combination': 'QOO',
        'support': True,
        'tasks' : ['retrieve_value', 'filter', 'derived_value', 'find_extremum', 'sort', 'distribution', 'find_anomalies', 'cluster'],
        'visualizations': ['barchart', 'scatterplot', 'stripplot'],
        'designs': [{
            'task': 'derived_value',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'sum'},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'derived_value',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'derived_value',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['size', 'x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': 'mean'}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'x', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['y', 'x', 'size'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'retrieve_value',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'retrieve_value',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'retrieve_value',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['size', 'x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'filter',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'filter',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'filter',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['size', 'x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
           'task': 'find_extremum',
           'vis_type': 'boxplot',
           'not_suggested_by_default': False,
           'mark': 'boxplot',
           'mandatory': ['x', 'y', 'color'],
           'priority': ['x', 'y', 'color'],
           'x': {'is_defined': False, 'agg': None, "scale": {"zero": False}},
           'y': {'is_defined': False, 'agg': None},
           'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'find_extremum',
            'vis_type': 'boxplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['x', 'y', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None, "scale": {"zero": False}},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'sort',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'sort',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'find_anomalies',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['size', 'x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'cluster',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'x', 'color'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'cluster',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'cluster',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'size'],
            'priority': ['size', 'x', 'y'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, 'agg': None}
        }]
    },
    'QOT': {
        'combination': 'QOT',
        'support': True,
        'tasks' : ['distribution', 'trend'],
        # 'tasks' : ['retrieve_value', 'filter', 'find_extremum', 'sort', 'distribution', 'find_anomalies', 'cluster', 'find_anomalies', 'correlation', 'trend'],
        'visualizations': ['linechart', 'barchart', 'stripplot'],
        'designs': [{
            'task': 'trend',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'trend',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'trend',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'x', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'barchart',
            'not_suggested_by_default': False,
            'mark': 'bar',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'x', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': 'mean'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'column', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'column', 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'color'],
            'priority': ['y', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'stripplot',
            'not_suggested_by_default': False,
            'mark': 'tick',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['y', 'x', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': None}
        }]
    },
    'QTT': {
        'combination': 'QTT',
        'support': False,
        'designs': [],
        'tasks': [],
        'visualizations': []
    },
    'NNN': {
        'combination': 'NNN',
        'support': False,
        'designs': [],
        'tasks': [],
        'visualizations': []
    },
    'NNO': {
        'combination': 'NNO',
        'support': False,
        'designs': [],
        'tasks': [],
        'visualizations': []
    },
    'NNT': {
        'combination': 'NNT',
        'support': True,
        'tasks' : ['retrieve_value', 'filter', 'distribution', 'cluster', 'trend'],
        'visualizations': ['linechart', 'scatterplot'],
        'designs': [{
            'task': 'trend',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['column', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['column', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'column', 'size'],
            'priority': ['x', 'y', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, "attr_ref": "x", "agg": "count"}
        }, {
            'task': 'retrieve_value',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'column', 'size'],
            'priority': ['x', 'y', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
        }, {
            'task': 'filter',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'column', 'size'],
            'priority': ['x', 'y', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
        }, {
            'task': 'cluster',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'column', 'size'],
            'priority': ['x', 'y', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
        }]
    },
    'NOO': {
        'combination': 'NOO',
        'support': False,
        'designs': [],
        'tasks': [],
        'visualizations': []
    },
    'NOT': {
        'combination': 'NOT',
        'support': True,
        'tasks' : ['retrieve_value', 'filter', 'distribution', 'cluster', 'trend'],
        'visualizations': ['linechart', 'scatterplot'],
        'designs': [{
            'task': 'trend',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['column', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['column', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'column', 'size'],
            'priority': ['x', 'y', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, "attr_ref": "x", "agg": "count"}
        }, {
            'task': 'retrieve_value',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'column', 'size'],
            'priority': ['x', 'y', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
        }, {
            'task': 'filter',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'column', 'size'],
            'priority': ['x', 'y', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
        }, {
            'task': 'cluster',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'column', 'size'],
            'priority': ['x', 'y', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
        }]
    },
    'NTT': {
        'combination': 'NTT',
        'support': False,
        'designs': [],
        'tasks': [],
        'visualizations': []
    },
    'OOO': {
        'combination': 'OOO',
        'support': False,
        'designs': [],
        'tasks': [],
        'visualizations': []
    },
    'OOT': {
        'combination': 'OOT',
        'support': True,
        'tasks' : ['retrieve_value', 'filter', 'distribution', 'cluster', 'trend'],
        'visualizations': ['linechart', 'scatterplot'],
        'designs': [{
            'task': 'trend',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['column', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        },{
            'task': 'distribution',
            'vis_type': 'linechart',
            'not_suggested_by_default': False,
            'mark': 'line',
            'mandatory': ['x', 'y', 'column', 'color'],
            'priority': ['column', 'color', 'x'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'attr_ref': 'x', 'agg': 'count'},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'color': {'attr': None, 'is_defined': False, 'agg': None}
        }, {
            'task': 'distribution',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'column', 'size'],
            'priority': ['x', 'y', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
            'size': {'attr': None, 'is_defined': False, "attr_ref": "x", "agg": "count"}
        }, {
            'task': 'retrieve_value',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'column', 'size'],
            'priority': ['x', 'y', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
        }, {
            'task': 'filter',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'column', 'size'],
            'priority': ['x', 'y', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
        }, {
            'task': 'cluster',
            'vis_type': 'scatterplot',
            'not_suggested_by_default': False,
            'mark': 'point',
            'mandatory': ['x', 'y', 'column', 'size'],
            'priority': ['x', 'y', 'column'],
            'x': {'attr': None, 'is_defined': False, 'agg': None},
            'y': {'attr': None, 'is_defined': False, 'agg': None},
            'column': {'attr': None, 'is_defined': False, 'agg': None},
        }]
    },
    'OTT': {
        'combination': 'OTT',
        'support': False,
        'designs': [],
        'tasks': [],
        'visualizations': []
    },
    'TTT': {
        'combination': 'TTT',
        'support': False,
        'designs': [],
        'tasks': [],
        'visualizations': []
    }
}
