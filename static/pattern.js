$(document).ready(function(){
    $('#query').click(function(e){
        e.preventDefault();
        queryHandler();
    });
    $('#update').click(function(e){
        e.preventDefault();
        updateHandler();
    });
    $('#delete').click(function(e){
        e.preventDefault();
        deleteHandler();
    });
});

function queryHandler(){
    var url = "/pattern/" + $("#input_text").val();
//    alert(url);
    $.ajax({
        url: url,
        type: 'GET',
        success: function(data){
            $("#output_text").val(data);
        }
    });
}

function updateHandler(){
    var url = "/pattern";
    $.post(url, $("#form").serialize(), function(){
        alert("update successfully!");
    });
}

function deleteHandler(){
    alert("kidding~");
}