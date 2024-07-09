package main

import (
    "fyne.io/fyne/v2"
    "fyne.io/fyne/v2/app"
    "fyne.io/fyne/v2/container"
    "fyne.io/fyne/v2/widget"
)

func main() {
    app := app.New()
    w := app.NewWindow("File Explorer")

    // Create split container
    split := container.NewHSplit(nil, nil)

    // Create tree
    tree := widget.NewTree(
        func(uid string) (children []string) {
            if uid == "" {
                return []string{"root"}
            }
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

    // Create table
    table := widget.NewTable(
        func() (int, int) { return 3, 3 },
        func() fyne.CanvasObject {
            return widget.NewLabel("")
        },
        func(id widget.TableCellID, cell fyne.CanvasObject) {
            cell.(*widget.Label).SetText(fmt.Sprintf("Cell %d, %d", id.Row, id.Col))
        },
    )

    // Add widgets to split container
    split.Leading = tree
    split.Trailing = table
    split.SetOffset(0.3)

    w.SetContent(split)
    w.Resize(fyne.NewSize(800, 600))
    w.ShowAndRun()
}
