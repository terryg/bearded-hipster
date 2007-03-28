var Browser = {};
Browser.restripe = function() {
  var table = $('browser');
  if (table) {
    var trs = table.getElementsByTagName('tr');
    for (var i = 0; i < trs.length; i++) {
      // remove existing classnames first
      Element.removeClassName(trs[i], 'even');
      Element.removeClassName(trs[i], 'odd');
      clsname = (i % 2 == 0) ? 'even' : 'odd'
      Element.addClassName(trs[i], clsname); 
    }      
  }
}

// Note that some of the Toolbar methods depend on the
// toolbar_icons and toolbar_items arrays
Toolbar = {};
Toolbar.toggle = function(element, icon) {
  for (var i = 0; i < toolbar_icons.length; i++) {
    if (toolbar_icons[i] != icon) {
      Toolbar.dehighlight(toolbar_icons[i]);
    } else {
      if ($(icon).style.backgroundColor == 'white')
        Toolbar.dehighlight(toolbar_icons[i]);
      else {
        Toolbar.highlight(toolbar_icons[i]);
      }
    }
  }
  for (var i = 0; i < toolbar_items.length; i++) {
    if (toolbar_items[i] != element) {
      Element.hide(toolbar_items[i]);
    } else {
      if ($(element).style.display == 'none') {
        Element.show(toolbar_items[i])
      } else {
        Element.hide(toolbar_items[i])
      }
    }
  }
}
Toolbar.hide = function(element, icon) {
  Element.hide(element);
  Toolbar.dehighlight(icon);
}
Toolbar.show = function(element, icon) {
  Element.show(element);
  Toolbar.highlight(icon)
}
Toolbar.hide_all = function() {
  for (var i = 0; i < toolbar_icons.length; i++) {
    Toolbar.dehighlight(toolbar_icons[i]);
  }
  for (var i = 0; i < toolbar_items.length; i++) {
    Element.hide(toolbar_items[i]);
  }
}  
Toolbar.highlight = function(element) {
  element = $(element);
  element.style.backgroundColor = 'white';
}
Toolbar.dehighlight = function(element) {
  element = $(element);
  element.style.backgroundColor = 'transparent';
}


Toolbar.Clipboard = Class.create();
Toolbar.Clipboard.update_count = function() {
  element = $('file-shelf-items');
  if (!element) {
    $('file-shelf-count').innerHTML = ''; 
    return;
  }
  if (children = element.getElementsByTagName('li')) {
    $('file-shelf-count').innerHTML = (children.length == 0 ? '' : ' (' + children.length + ')');
  } else {
    $('file-shelf-count').innerHTML = '';
  }
}
Toolbar.Clipboard.has_item = function(class_name) {
  items = $('file-shelf-items');
  if (!items) return; 
  if (children = items.getElementsByTagName('li')) {
    for (var i = 0; i < children.length; i++) {
      if (children[i].id == 'item_' + class_name) return true;
    }
  }
  return false;
}
Toolbar.Clipboard.has_selected_elements = function() {
  boxes = Form.getInputs('items_form', 'checkbox', 'files[]');
  for (var i = 0; i < boxes.length; i++) {
    if (boxes[i].checked) return true;
  }
  return false;
}
Toolbar.Clipboard.show_buttons_if_selected = function() {
  button_element = 'copy-move-buttons';
  info_element = 'copy-move-info';
  if (Toolbar.Clipboard.has_selected_elements()) {
    Element.show(button_element);
    Element.hide(info_element);
  } else{
    Element.hide(button_element);
    Element.show(info_element);
  }
}


