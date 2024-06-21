# Load necessary libraries
install.packages("ggplot2")
library(ggplot2)

# Create a simple data frame
data <- data.frame(
  x = 1:10,
  y = rnorm(10)
)

# Plot the data
ggplot(data, aes(x = x, y = y)) +
  geom_point() +
  geom_smooth(method = "lm")

# Calculate the mean of y
mean_y <- mean(data$y)
print(mean_y)
