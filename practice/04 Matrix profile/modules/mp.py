import numpy as np
import pandas as pd
import math

import stumpy
from stumpy import config


def compute_mp(ts1: np.ndarray, m: int, exclusion_zone: int = None, ts2: np.ndarray = None):
        """
        Compute the matrix profile

        Parameters
        ----------
        ts1: the first time series
        m: the subsequence length
        exclusion_zone: exclusion zone
        ts2: the second time series

        Returns
        -------
        output: the matrix profile structure
                (matrix profile, matrix profile index, subsequence length, exclusion zone, the first and second time series)
        """
        if ts2 is None:
                # Если ts2 не указан, считаем матричный профиль для одного ряда
                mp = stumpy.stump(ts1, m, k=exclusion_zone)
        else:
                # Если указан ts2, вычисляем матричный профиль между двумя временными рядами
                mp = stumpy.stump(ts1, m, ts2)

        return {'mp': mp[:, 0],
                'mpi': mp[:, 1],
                'm' : m,
                'excl_zone': exclusion_zone,
                'data': {'ts1' : ts1, 'ts2' : ts2}
                }
