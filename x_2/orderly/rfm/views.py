import os

from django.http import JsonResponse

import pandas as pd


def rfm_sort(request):

    sort_by = request.GET.get('sort_by', "recency")

    module_dir = os.path.dirname(__file__)

    file_path = os.path.join(module_dir, r'static\rfm\rfm.csv')

    dtypes = {'ID': 'int',
              'R': 'int',
              'F': 'int',
              'M': 'int'}

    table = pd.read_csv(file_path,
                        sep=',',
                        header=0,
                        dtype=dtypes)

    table.loc[:, "RFM"] = table["R"] + table["F"] + table["M"]

    if sort_by == "recency":
        _values = table.sort_values(by=['R', 'ID'], ascending=[False, True])["ID"].values
        return JsonResponse(_values.tolist(), safe=False)
    elif sort_by == "frequency":
        _values = table.sort_values(by=['F', 'ID'], ascending=[False, True])["ID"].values
        return JsonResponse(_values.tolist(), safe=False)
    elif sort_by == "monetary":
        _values = table.sort_values(by=['M', 'ID'], ascending=[True, True])["ID"].values
        return JsonResponse(_values.tolist(), safe=False)
    elif sort_by == "rfm":
        _values = table.sort_values(by=['RFM', 'ID'], ascending=[False, True])["ID"].values
        return JsonResponse(_values.tolist(), safe=False)
