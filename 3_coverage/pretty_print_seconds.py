def pretty_print_seconds(seconds, n_labels=0, separator=" "):
    """
    Converts a number of seconds to a readable time string.

    Parameters
    ----------
    seconds : float or int
        number of seconds to represent, gets rounded with int()
    n_labels : int
        number of levels of label to show. For example, if n_labels=1,
        result will show the first of days, hours, minutes, seconds with
        greater than one. This allows you to round, e.g, 1 day 2 hours
        3 minutes 4 seconds to 1 day 2 hours (with n_labels=2). Default
        value of 0 gives all levels. If n_labels is negative, then the last
        value is shown as a decimal, instead of an int, with 2 decimals of
        precision.
    separator : string
        separator between levels of the time decomposition
    """
    ordered_keys = ['day', 'hour', 'minute', 'second']
    divisors = {
        'day': 86400,
        'hour': 3600,
        'minute': 60,
        'second': 1
    }

    s = int(seconds)

    def decompose_seconds(s):
        parts = {}
        fractional_parts = {}
        for k in ordered_keys:
            fractional_parts[k] = float(s) / divisors[k]
            parts[k], s = divmod(s, divisors[k])
        return parts, fractional_parts

    def make_seconds(parts):
        return sum([parts[p] * divisors[p] for p in parts.keys()])

    parts, fractional_parts = decompose_seconds(s)

    decimalize_final = (n_labels < 0)

    first_key = "second"
    for key in ordered_keys:
        if parts[key] > 0:
            first_key = key
            break
    first_key_index = ordered_keys.index(first_key)

    n_labels_real = len(ordered_keys) - first_key_index
    if n_labels != 0 and abs(n_labels) < n_labels_real:
        n_labels_real = abs(n_labels)

    max_label_index = first_key_index + len(ordered_keys) - n_labels_real
    if max_label_index >= len(ordered_keys):
        max_label_index = len(ordered_keys) - 1
    max_label = ordered_keys[max_label_index]

    if first_key != "second" and n_labels > 0:
        # round it!
        if fractional_parts[max_label] - parts[max_label] >= 0.5:
            parts[max_label] += 1
        else:
            pass
        for key in ordered_keys[max_label_index + 1:]:
            parts[key] = 0

    new_s = make_seconds(parts)
    parts, frac_parts = decompose_seconds(new_s)

    part_labels = {k: k if parts[k] == 1 else k + "s"
                   for k in ordered_keys}

    label_count = 0
    output_str = ""
    for key in ordered_keys[first_key_index:]:
        part = parts[key]
        label_str = part_labels[key]
        frac = fractional_parts[key]
        if part > 0 and label_count < n_labels_real - 1:
            output_str += str(part) + " " + label_str + separator
            label_count += 1
        elif label_count == n_labels_real - 1:
            if decimalize_final and key != 'second':
                output_str += "%.2f %s" % (frac, key+'s')
            else:
                output_str += str(part) + " " + label_str
            label_count += 1

    return output_str

