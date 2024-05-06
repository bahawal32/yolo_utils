    """
    Convert normalized bounding box coordinates from center and dimensions to top-left and bottom-right corners.
    
    Parameters
    ----------
    x : float
        x-coordinate of the center of the bounding box
    y : float
        y-coordinate of the center of the bounding box
    w : float
        width of the bounding box
    h : float
        height of the bounding box
    
    Returns
    -------
    list
        List containing the coordinates of the top-left and bottom-right corners of the bounding box
    """
    """
    Convert normalized bounding box coordinates to integer values based on image width and height.
    
    Parameters
    ----------
    width : int
        Width of the image
    height : int
        Height of the image
    line_point : list
        List containing the normalized coordinates of the bounding box
    
    Returns
    -------
    tuple
        Tuple containing the integer coordinates of the top-left and bottom-right corners of the bounding box
    """
    # Blue color in BGR
    color = (255, 0, 0)
    
    # Line thickness of 2 px
    thickness = 2
    
    # Draw bounding boxes on the image
    for i, det in enumerate(pred):
        for *xyxy, conf, cls in reversed(det):
            xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
            line = (cls, *xywh)  # label format
            x,y,w,h = line[1], line[2], line[3], line[4]
            line_point = convert_mid_to_corner(x,y,w,h)
            x1,y1,x2,y2 = convert_to_int(width, height,line_point)
            cv2.rectangle(img0,(x1, y1), (x2, y2),color,thickness)
            cv2.imshow('test',img0)
            cv2.waitKey(0)
```