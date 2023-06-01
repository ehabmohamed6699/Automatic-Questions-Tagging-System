import flet as ft
import joblib

clf = joblib.load("SVMClassifier.sav")
binarizer = joblib.load("Binarizer.sav")
tfidf = joblib.load("TFIDF.sav")

def classify(title, body):
    tt = tfidf.transform([title])
    bt = tfidf.transform([body])
    tt = tt.toarray().tolist()
    bt = bt.toarray().tolist()
    tt = tt[0]
    tt.extend(bt[0])
    res = clf.predict([tt])
    return binarizer.inverse_transform(res)[0]

tagsTexts = []



def main(page: ft.Page):
    page.title = "Automatic question tagging system"
    page.bgcolor = ft.colors.TERTIARY_CONTAINER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    suggestedTitle = ft.Text(value="", size=30, italic=True)


    def updatedSuggestedTags(e):
        title = questionTitle.value
        body = questionBody.value
        tags = classify(title=title,body=body)
        tagsTexts.clear()
        tagsTexts.append(ft.Text(value='Suggested Tags: ', size=30,))
        for tag in tags:
            tagsTexts.append(ft.Text(value=tag, size=30, italic=True))
        suggestedTitle.value = 'Tag: '+title+body
        page.update()

    questionTitle = ft.TextField(value="", text_align=ft.TextAlign.CENTER, width=300, hint_text="Enter question title")
        
    questionBody = ft.TextField(value="", text_align=ft.TextAlign.CENTER, width=300, hint_text="Enter question body")
        
    button = ft.ElevatedButton(text="Update tags", on_click=updatedSuggestedTags, width=200)

    

    page.add(
        ft.Row( [
        ft.Column(
        [
            ft.Row([
                ft.Container(
                ft.Text(value='Title', size=30,),
                width=100
                ),
                questionTitle,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row([
                ft.Container(
                ft.Text(value='Body', size=30,),
                width=100
                ),
                questionBody,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
            [
                button,  
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            ),
            
        ],
            alignment=ft.MainAxisAlignment.CENTER,

        ),
         ft.Row(
            [
            ft.Container(width=30),    
            ft.Column(
            tagsTexts  
            ,
            alignment=ft.MainAxisAlignment.CENTER,
            )],
            alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)