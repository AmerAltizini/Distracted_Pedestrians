# sliding window algorithm
import pandas as pd
from .ExtractFeatures import compute_features


#Implements a sliding window approach with given window size and overlap
def sliding_window(data, cols, windowsize, overlap=0.5, start_ts=None, label=False,):
    '''
    returns the features calculated by using sliding window
    :param data: pandas DataFrame containing the data to be segmented and features calculated on
    :param cols: columname containing the data
    :param windowsize: windowsize in milliseconds
    :param overlap: overlap between 0 and 1 - default is 50%
    :param start_ts: timestamp to start segmentation
    :param label: check if label is handed over -> add mayority vote
    :return: calcuated features
    '''

    if data.shape[0] < 1:
        return None
    if type(overlap) != type(0.0) or type(windowsize) != type(0):
        raise Exception('**Error** type(overlap) must be float and type(windowsize) must be int')
    if overlap > windowsize:
        raise Exception('**Error** overlap is larger than windowsize...')

    # Creating chunks
    if "IBI" in cols:
        header = ['mean_nni', 'sdnn', 'sdsd', 'nni_50', 'pnni_50', 'nni_20', 'pnni_20', 'rmssd','median_nni', 'range_nni',
                  'cvsd', 'cvnni', 'mean_hr', 'max_hr', 'min_hr', 'std_hr', 'triangular_index', 'lf', 'hf', 'lf_hf_ratio',
                  'lfnu', 'hfnu', 'total_power', 'vlf', 'sd1', 'sd2', 'ratio_sd2_sd1',
                  'window_ts']
    else:
        # Creating chunks
        suffix = ['slope', 'sqrtSlope', 'sqrtIntersect', 'thirdSqrtIntersect']
        header1 = ['{}_{}'.format(col, suf) for col in cols for suf in suffix]
        suffix = ['var', 'std', 'skew', 'rms', 'min', 'max', 'mean', 'median']
        header2 = ['{}_{}'.format(col, suf) for col in cols for suf in suffix]
        header = header1 + header2 + ['window_ts']
        if "GSR" in cols:
            headerSCR = ['SCR_peaknumber','SCR_meanpeakhight','SCR_sumresponseduration']
            header = header1 + headerSCR +  header2 + ['window_ts']

    if  label:
        header =  header + ["label"]

    result = pd.DataFrame(columns=header)

    # set timing parameters
    # step is the time the window slides forward
    step = int(windowsize * (1 - overlap))
    if start_ts != None:
        start = start_ts
    else:
        start = data['time'].iloc[0]
    # grap last instance of dataset as end time
    end = data.last_valid_index()

    # get windows
    while start < end:
        row_result = []
        window = data[(data.index >= start) & (start + windowsize >= data.index)]

        # does window contain data
        if window.shape[0] > 1:  # needs more than one element in window
            if 'IBI' in cols:
                # row_result = get_IBI_features(window)
                row_result['window_ts'] = start
                # labels - labels hinzufügen
                if label:
                    row_result.append(pd.value_counts(window['label']).idxmax())
                result = result.append(row_result)
            else:
                # start statistical feature calculation
                row_result = compute_features(window, cols)
                row_result.append(start)
                # labels - labels hinzufügen
                if label:
                    row_result.append(pd.value_counts(window['label']).idxmax())
                # add window to final result
                result.loc[len(result)] = row_result
        start = start + step
    return result