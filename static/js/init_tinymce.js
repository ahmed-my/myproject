document.addEventListener('DOMContentLoaded', function() {
    tinymce.init({
        selector: 'textarea.tinymce',
        height: 500,
        width: 800,
        cleanup_on_startup: true,
        custom_undo_redo_levels: 20,
        theme: 'modern',
        plugins: 'textcolor save link image media preview codesample contextmenu table code lists fullscreen insertdatetime nonbreaking directionality searchreplace wordcount visualblocks visualchars autolink lists charmap print hr anchor pagebreak',
        toolbar1: 'fullscreen preview bold italic underline | fontselect fontsizeselect | forecolor backcolor | alignleft alignright | aligncenter alignjustify | indent outdent | bullist numlist table | link image media | codesample code', // code included here
        toolbar2: 'visualblocks visualchars | charmap hr pagebreak nonbreaking anchor | save | searchreplace wordcount | insertdatetime media',
        menubar: 'file edit view insert format tools table help', // Menubar added for more control
        contextmenu: "link image inserttable | cell row column deletetable | code", // Context menu support for code
        setup: function (editor) {
            editor.on('init', function () {
                editor.formatter.register('code', {
                    inline: 'code'
                });
            });
        },
        directionality: 'ltr',
        strict_loading_mode: 1
    });
});
