$(document).ready(function(){
    // $(".shkarp").submit(function(e){
    //     e.preventDefault()
    // })
    $(document).on('click' , '#delete' , function(e){
        e.preventDefault();
        var btn = $(this)
        var product_id = btn.data('product_id')
        var product_name = btn.data('product_name')
        var product_price = btn.data('product_price')
        var product_number = btn.data('product_number')
        var amount = btn.data('products_amount')
        var product_total_price = btn.data('product_total_price')
        console.log(product_name , product_price , product_number , product_total_price , product_id , is_delete=true , 'LOOL')
        basket(product_name , product_price , product_number , product_total_price , product_id , is_delete=true)
        $(this).parent().remove()
        var t = 0
        $(".numbers_of_product").each(function() {
            t = t + 1
            var btn2 = $(this)
            pid = btn2.data('product_id')
            console.log(t , pid , product_id)
            if (pid = parseInt(product_id)){
                $(".class" + pid).parent().parent().remove()
                console.log("class" + pid)
            }
        });




        for (var i = 0 ; i < amount; i = i + 1){
            if (product_id == i){
                
            }
        }
        console.log('Holla')
    })

    $(".busket_a").click(function(){
        $(".busket_div").toggle()
    });

    $(".busket_a2").click(function(){
        $(".busket_div").toggle()
        $(".busket_div").css('top' , '1000%')
        var parentElement = $(".nav-wrapper")
        var parentWidth = parentElement.width();
        $(".busket_div").width(parentWidth);
        $(".busket_div").css('overflow' , 'scroll')
        $(".busket_div").css('height' , '247px')
        // $(".busket_div").css('display' , 'block')

    });
    $(".hamburger div").click(function(){
        $(".busket_div").css('display' , 'none') 
    })


    var form = $('.main_form')
    $(form).submit(function(e){
        e.preventDefault()
        var btn = $('#needed_btn')
        var product_name = btn.data('product_name')
        var product_id = btn.data('product_id')
        var product_price = btn.data('product_price')
        var product_number = $("#number").val()
        var product_total_price = product_price * product_number
        basket(product_name , product_price , product_number , product_total_price , product_id , is_delete=false)
    })
    var js_data = {}

    function basket(product_name , product_price , product_number , product_total_price , product_id , is_delete){
    
        var url = $('.main_form').attr('action')
        var csrf_token = $('.buy').prev().val()
        js_data['csrfmiddlewaretoken'] = csrf_token
        js_data['product_name'] = product_name
        js_data['product_price'] = product_price
        js_data['product_number'] = product_number
        js_data['product_total_price'] = product_total_price
        js_data['product_id'] = product_id
        js_data['is_delete'] = is_delete
        console.log(js_data , 'js_data' , 'URL' , url)

        $.ajax({
            data : js_data,
            url : url,
            type : 'POST',
            cache : true,
            success : function(python_data){
                $('.busket_ul').text(' ')
                console.log(python_data['products_in_basket'] , 'python_data')
                $.each((python_data['products_in_basket']) , function(index , value){
                    $(".busket_ul").append('<li>' + value.product_name + ' ' 
                                                  + value.product_price + '$'  
                                                  + ' ' + 'x' + ' ' 
                                                  + value.number + ' ' 
                                                  + value.product_total_price + '$' + ' ' 
                                                  + '<a id="delete" data-product_id = " '+value.product_id+' " data-product_name = " '+value.product_name+' " data-product_price = " '+value.product_price+' " data-product_number = " '+value.number+' " data-product_total_price = " '+value.product_total_price+' ">X</a>' + '</li>')
                })
                $(".arbitrary").text('[' + python_data['number_of_products'] + ']')
                if (python_data['number_of_products'] == 0){
                    $(".busket_ul").append('<p style="font-size: 16px;"> You have not added products yet</p>')
                }
            },
            error : function(){
                console.log('error')
            }

        })
    }
    function calculating(){
        var products_total_amount = 0
        $(".product_total_price").each(function(){
            products_total_amount += parseInt($(this).text())
            console.log(products_total_amount)
        })
        $("#product_total_amount").text(products_total_amount)
    }
    function calculating2(){
        $(".numbers_of_product").on('change' , function(){
            var currant_price = $(this).closest('td').prev().text()
            var number = $(this).val()
            var price = parseInt(currant_price) * number
            console.log(number ,' , ', price , ' , ', currant_price)
            $(this).closest('td').next().find('span').text(price);
            var products_total_amount = 0
            $(".product_total_price").each(function(){
                products_total_amount += parseInt($(this).text())
                console.log(products_total_amount)
            })
            $("#product_total_amount").text(products_total_amount)
        })
    }
    function calculating3(){
        $(document).on('click' , '#delete' , function(e){
        var btn = $(this)
        var number = btn.data('product_number')
        var pricer = btn.data('product_price')
        var price = number * pricer
        var total = parseFloat($("#product_total_amount").text())
        var minus = total - parseFloat(price)
        $("#product_total_amount").text(minus)
        
        })
        console.log(1231)
    }
    $(document).on('change' , '.numbers_of_product' , function(e){
        e.preventDefault()
        var btn = $(this)
        var product_name = btn.data('product_name')
        var product_id = btn.data('product_id')
        console.log(product_id , 'SOSEM , R O M')
        var product_price = btn.data('product_price')
        var product_number = $(this).val()
        var product_total_price = product_price * product_number
        basket(product_name , product_price , product_number , product_total_price , product_id , is_delete='emergency')
    })
    calculating()
    calculating2()
    calculating3()
    $(".humburger").click(function() {
        $('#kk').css("position" , "absolute") ;
        $('#kk').css("top" , "47px");
        $('#kk').css("object-fit" , "cover");
        $('#kk').css("height" , "60x");
        $(".navv").css("height" , "200px");
        $(".middle").css("display" , "block");
        $(".right").css("display" , "block");
        $("#humburger").css("display" , "none")
        $("#humburger-2").css("display" , "block")
    })
    $(".humburger-2").click(function() {
        $(".f_img").css('height' , '38px')
        $(".f_img").css('top' , '10px')
        $(".middle").css("display" , "none");
        $(".right").css("display" , "none");
        $(".navv").css('height' , '100px')
        $("#humburger-2").css("display" , "none")
        $("#humburger").css("display" , "block")
    })
    $("#soak").click(function(e){
        // $(this).css('display' , 'none')
        $(".megan_beer").parent().parent().parent().parent().css('display' , 'none')
    })
    $("#ava").click(function(e){
        $("#ava1").css('display' , 'block')
        $("#all1").css('display' , 'none')
    })
    $("#all").click(function(e){
        $("#all1").css('display' , 'block')
        $("#ava1").css('display' , 'none')
    })
})
