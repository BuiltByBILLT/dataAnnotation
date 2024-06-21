# library(shiny)
# library(shinydashboard)
# library(ggplot2)
# library(dplyr)
# library(DT)


# ui <- dashboardPage(
#   dashboardHeader(title = "Habit Tracker"),
#   dashboardSidebar(
#     dateInput("date", "Select Date:", value = Sys.Date()),
#     selectInput("habit", "Select Habit:", choices = c("Exercise", "Reading", "Meditation", "Coding")),
#     numericInput("duration", "Duration (minutes):", value = 0, min = 0),
#     actionButton("add_record", "Add Record")
#   ),
#   dashboardBody(
#     fluidRow(
#       box(title = "Habit Data", DT::dataTableOutput("habit_data_table"), width = 12)
#     ),
#     fluidRow(
#       box(title = "Habit Progress", plotOutput("habit_plot"), width = 12)
#     )
#   )
# )

# server <- function(input, output) {
#   habit_data <- reactiveValues(data = data.frame(Date = as.Date(character()), Habit = character(), Duration = numeric(), stringsAsFactors = FALSE))

#   observeEvent(input$add_record, {
#     new_record <- data.frame(
#       Date = input$date,
#       Habit = input$habit,
#       Duration = input$duration
#     )
#     habit_data$data <- rbind(habit_data$data, new_record)
#   })

#   output$habit_data_table <- DT::renderDataTable({
#     habit_data$data
#   })

#   output$habit_plot <- renderPlot({
#     habit_data$data %>%
#       ggplot(aes(x = Date, y = Duration, color = Habit)) +
#       geom_line() +
#       geom_point() +
#       labs(title = "Habit Tracking Progress", x = "Date", y = "Duration (minutes)")
#   })
# }
# shinyApp(ui, server)