def stock_availability(boxes, *args):
    action = args[0]

    if action == "delivery":
        boxes.extend(args[1:])

    else:
        arguments = args[1:]

        if len(arguments) == 0:
            boxes.pop(0)

        else:

            try:
                boxes = boxes[arguments[0]:]

            except TypeError:
                for flavor in arguments:
                    if flavor in boxes:
                        while flavor in boxes:
                            boxes.remove(flavor)

    return boxes