package main

import (
    "fmt"
    "os"
    "path/filepath"
    "io/ioutil"
    "fyne.io/fyne/v2/app"
    "fyne.io/fyne/v2/container"
    "fyne.io/fyne/v2/widget"
)

func main() {
    a := app.New()
    w := a.NewWindow("File Explorer")

    navigation := widget.NewTree(
        func(uid string) (children []string) {
            if uid == "" {
                return []string{"root"}
            }
            // Assume "root" is the only node for simplicity
            return nil
        },
        func(uid string) bool {
            return uid == "root"
        },
        func(branch bool, uid string) fyne.CanvasObject {
            return widget.NewLabel(uid)
        },
        func(uid string, node fyne.CanvasObject) {
            node.(*widget.Label).SetText(uid)
        },
    )

    content := widget.NewLabel("Content")

    split := container.NewHSplit(navigation, content)
    split.SetOffset(0.3)

    w.SetContent(split)
    w.Resize(fyne.NewSize(800, 600))
    w.ShowAndRun()
}
