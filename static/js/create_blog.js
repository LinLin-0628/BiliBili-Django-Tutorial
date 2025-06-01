window.onload = function() {

// Step 1: Access i18nChangeLanguage from wangEditor
    const { createEditor, createToolbar, i18nChangeLanguage } = window.wangEditor

    // Step 2: Set language to English BEFORE creating editor
    i18nChangeLanguage('en')

    const editorConfig = {
        placeholder: 'Type here...',
        onChange(editor) {
            const html = editor.getHtml()
            console.log('editor content', html)
// You can sync HTML to <textarea>
        }
    }

    const editor = createEditor({
        selector: '#editor-container',
        html: '<p><br></p>',
        config: editorConfig,
        mode: 'default', // or 'simple'
    })

    const toolbarConfig = {}

    const toolbar = createToolbar({
        editor,
        selector: '#toolbar-container',
        config: toolbarConfig,
        mode: 'default', // or 'simple'
    })

}