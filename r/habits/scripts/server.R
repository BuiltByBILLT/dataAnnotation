library(shiny)
library(dplyr)
library(ggplot2)


ui <- fluidPage(
  titlePanel("Daily Habits Tracker"),
  sidebarLayout(
    sidebarPanel(
      dateInput("date", "Date:", value = Sys.Date()),
      checkboxGroupInput("habits", "Select Completed Habits:",
                         choices = c("Exercise", "Read", "Meditate")),
      actionButton("submit", "Submit")
    ),
    mainPanel(
      plotOutput("habitPlot")
    )
  )
)

server <- function(input, output) {
  
  # A reactive value to store the habits data
  habitsData <- reactiveVal(data.frame(Date = as.Date(character()), 
                                       Habit = character(), 
                                       stringsAsFactors = FALSE))
  
  observeEvent(input$submit, {
    # Update the habits data when a new submission is made
    newEntry <- data.frame(Date = rep(input$date, length(input$habits)), 
                           Habit = input$habits, 
                           stringsAsFactors = FALSE)
    habitsData(rbind(habitsData(), newEntry))
  })
  
  output$habitPlot <- renderPlot({
    data <- habitsData()
    
    # Simple visualization: count of habits over time
    ggplot(data, aes(x = Date, fill = Habit)) +
      geom_bar(stat = "count", position = "dodge") +
      labs(title = "Habit Completion Over Time", x = "Date", y = "Count") +
      theme_minimal()
  })
}

shinyApp(ui = ui, server = server)