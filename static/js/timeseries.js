$(function() {
 
var common_constraints_enabled = true;
var curve_num = 0;

function check_common_constraint_condition()
{
    common_constraints_enabled = true;
    module = $("#curve_1_module_instance option:selected").val();
    subtable = $("#curve_1_subtable option:selected").val();
    for(var i=2; i<= curve_num; i += 1) {
        if($("#curve_"+i+"_module_instance option:selected").val() != module
            || $("#curve_"+i+"_subtable option:selected").val() != subtable) {
            common_constraints_enabled = false;
            break;
        }
    }
            
    if(common_constraints_enabled)
        $('#common_constraints_info').fadeOut(250);
    else
        $('#common_constraints_info').fadeIn(250);
}

function changed_subtable(e)
{
    curve = e.data.curve;
    var module = $("#"+curve+"_module_instance option:selected").val();
    var subtable = $("#"+curve+"_subtable option:selected").val();
   
    var html = "";
    for(var idx in modules[module][subtable]) {
        if(idx == 0)
            html += " <option selected=\"selected\">";
        else
            html += " <option>"
        html += modules[module][subtable][idx] + "</option>";
    }
    $("#"+curve+"_variable").empty().append(html);
    check_common_constraint_condition();
}

function changed_module(e)
{
    curve = e.data["curve"];
    var module = $("#"+curve+"_module_instance option:selected").val();
   
    var html = "";
    for(var subtable in modules[module]) {
        html += " <option>" + subtable + "</option>";
    }
    $("#"+curve+"_subtable").empty().append(html);
    changed_subtable(e);
    check_common_constraint_condition();
}

function add_curve(initial_mod, initial_table, initial_variable, initial_title) {
    curve_num += 1;
    html  = "<fieldset class=\"floating\"><legend>Curve "+curve_num+"</legend>";
    html += " <p><label><span>Module</span><select id=\"curve_"+curve_num+"_module_instance\" name=\"curve_"+curve_num+"_module_instance\">";
    var first_mod = initial_mod;
    for(var mod in modules) {
        if(first_mod == "") first_mod = mod;
        if(first_mod == mod) html += " <option selected=\"selected\"";
        else html += " <option";
        html += " value=\"" + mod + "\">" + mod + " (" + module_types[mod] + ")</option>";
    }
    html += " </select></label></p>";
    html += " <p><label><span>Subtable</span><select id=\"curve_"+curve_num+"_subtable\" name=\"curve_"+curve_num+"_subtable\">";
    var found_subtable = false;
    for(var subtable in modules[first_mod]) {
        if(subtable == initial_table) {
            html += " <option selected=\"selected\">";
            found_subtable = true;
        }
        else
            html += " <option>";
        html += subtable + "</option>";
    }
    if(!found_subtable)
        initial_table = '';
    
    html += " </select></label></p>";
    html += " <p><label><span>Variable</span><select  id=\"curve_"+curve_num+"_variable\" name=\"curve_"+curve_num+"_variable\">";
    for(var idx in modules[first_mod][initial_table]) {
        if(modules[first_mod][initial_table][idx] == initial_variable)
            html += " <option selected=\"selected\">";
        else
            html += " <option>";
        html += modules[first_mod][initial_table][idx] + "</option>";
    }
    html += " </select></label></p>";
    html += " <p><label><span>Title</span><input id=\"curve_"+curve_num+"_title\" type=\"edit\" name=\"curve_"+curve_num+"_title\" value=\"";
    html += initial_title+"\"></label></p>";
    html += "<!--<p class='button_box floating'><a class='small add' href='#'>+</a><a class='small remove' href='#'>-</a></p>"
    html += "<h3>Constraints</h3>-->";
    html += "</fieldset>";
    $("#curve_controls").before(html);
    $("#curve_"+curve_num+"_module_instance").change({'curve': "curve_"+curve_num}, changed_module);
    $("#curve_"+curve_num+"_subtable").change({'curve': "curve_"+curve_num}, changed_subtable);
    
    return false;
}

function get_constraint_html(variable, data) {
    curve_num += 1;
    html  = "<fieldset class=\"floating\"><legend>Curve "+curve_num+"</legend>";
    html += " <p><label><span>Module</span><select id=\"curve_"+curve_num+"_module_instance\" name=\"curve_"+curve_num+"_module_instance\">";
    var first_mod = initial_mod;
    for(var mod in modules) {
        if(first_mod == "") first_mod = mod;
        if(first_mod == mod) html += " <option selected=\"selected\"";
        else html += " <option";
        html += " value=\"" + mod + "\">" + mod + " (" + module_types[mod] + ")</option>";
    }
    html += " </select></label></p>";
    html += " <p><label><span>Subtable</span><select id=\"curve_"+curve_num+"_subtable\" name=\"curve_"+curve_num+"_subtable\">";
    var found_subtable = false;
    for(var subtable in modules[first_mod]) {
        if(subtable == initial_table) {
            html += " <option selected=\"selected\">";
            found_subtable = true;
        }
        else
            html += " <option>";
        html += subtable + "</option>";
    }
    if(!found_subtable)
        initial_table = '';
    
    html += " </select></label></p>";
    html += " <p><label><span>Variable</span><select  id=\"curve_"+curve_num+"_variable\" name=\"curve_"+curve_num+"_variable\">";
    for(var idx in modules[first_mod][initial_table]) {
        if(modules[first_mod][initial_table][idx] == initial_variable)
            html += " <option selected=\"selected\">";
        else
            html += " <option>";
        html += modules[first_mod][initial_table][idx] + "</option>";
    }
    html += " </select></label></p>";
    html += " <p><label><span>Title</span><input id=\"curve_"+curve_num+"_title\" type=\"edit\" name=\"curve_"+curve_num+"_title\" value=\"";
    html += initial_title+"\"></label></p>";
    
    html += "</fieldset>";
    $("#curve_controls").before(html);
    $("#curve_"+curve_num+"_module_instance").change({'curve': "curve_"+curve_num}, changed_module);
    $("#curve_"+curve_num+"_subtable").change({'curve': "curve_"+curve_num}, changed_subtable);
    
    return false;
}

$("#add_curve").click(function() {add_curve('', '', '', '') });
$("#remove_curve").click(function() {
    if(curve_num > 1) {
        $("#curve_controls").prev().remove();
        curve_num -= 1;
    }
    return false;
});

$("#show_curve_form").click(function() {
    $("#curve").slideDown();
    $("#show_curve_form").hide();
    $("#hide_curve_form").show();
    return false;
});
$("#hide_curve_form").click(function() {
    $("#curve").slideUp();
    $("#show_curve_form").show();
    $("#hide_curve_form").hide();
    return false;
});

$("#update_plot").click(function() {
    var html = "";
    for(var i=1; i <= curve_num; i++)
    {
        var id_particle = "#curve_"+i;
        var mod = $(id_particle+"_module_instance option:selected").val();
        var table = $(id_particle+"_subtable option:selected").val();
        var variable = $(id_particle+"_variable option:selected").val();
        var title = $(id_particle+"_title").val();
        html += "<input type=\"hidden\" name=\"curve_"+i+"\" value=\""+mod+","+table+","+variable+","+title+"\" />\n";
    }
    $("#plot_inputs").empty().append(html);
    $("#plot_form").submit();
    return false;
});


for(var idx in curves) {
    add_curve(curves[idx][0], curves[idx][1], curves[idx][2], curves[idx][3]);
}

if(curve_num == 0)
    add_curve('', '', '', '');

});