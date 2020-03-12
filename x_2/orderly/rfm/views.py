import os

from django.http import JsonResponse

import pandas as pd


def rfm_sort(request):
    """
    根據request物件中的sort_by parameter去進行rfm.csv檔案的id排序
    eg. http://xxx.xxx.com/rfm-sort/?sort_by=recency

    如果sort_by是 recency, 將 ID 以倒 R 值排序回傳 (大到小)
    如果sort_by是 frequency, 將 ID 以倒 F 值排序回傳 (大到小)
    如果sort_by是 monetary, 將 ID 以 M 值排序回傳 (小到大)
    如果sort_by是 rfm, 將 ID 以倒 RFM 總值排序回傳
    ps. 如果排序對象數值相同, 再以id由小到大的順序排列

    :param request:
    :return: json
    """
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
