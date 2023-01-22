def has_label_check(has_label, label):
    if has_label == 'true' and label is not None:
        return label
    elif has_label == 'true' and label is None:
        return 'Viewers'
    elif has_label == 'false' and label is None:
        return ''
    elif has_label == 'false' and label is not None:
        return ''
    else:
        return 'Viewers'
