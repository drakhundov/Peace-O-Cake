function auto_height(elem, default_size) {
    if (Math.abs(elem.scrollHeight - default_size) < default_size * 0.1)
        return
    elem.style.height = default_size+"px"
    elem.style.height = (elem.scrollHeight)+"px"
}
