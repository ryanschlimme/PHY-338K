library(tidyverse)
library(mosaic)
library(patchwork)

# Full Time Domain Constant Detrend
# Subtracting 10 Ohm Data (representing noise of entire system)
avgV10 = mean(~V10, data = Lab9Data)
avgV47k = mean(~V47k, data = Lab9Data)
avgV94k = mean(~V94k, data = Lab9Data)
avgV220k = mean(~V220k, data = Lab9Data)
avgV672k = mean(~V672k, data = Lab9Data)

Lab9Data = Lab9Data %>% 
  mutate(newV10 = V10 - avgV10,
         newV47k = V47k - avgV47k - newV10,
         newV94k = V94k - avgV94k - newV10,
         newV220k = V220k - avgV220k - newV10,
         newV672k = V672k - avgV672k - newV10)

# RMS Voltage Summaries
sdV10 = sd(~newV10, data = Lab9Data)
sdV47k = sd(~newV47k, data = Lab9Data)
sdV94k = sd(~newV94k, data = Lab9Data)
sdV220k = sd(~newV220k, data = Lab9Data)
sdV672k = sd(~newV672k, data = Lab9Data)


# Histograms
p1 = ggplot(Lab9Data) +
  geom_histogram(aes(x = newV10)) +
  coord_cartesian(xlim = c(-0.03, 0.03), ylim = c(0, 320)) +
  labs(x = "",
       y = "Counts",
       subtitle = "10 Ohm, RMS = 5.28 mV")

p2 = ggplot(Lab9Data) +
  geom_histogram(aes(x = newV47k)) +
  coord_cartesian(xlim = c(-0.03, 0.03), ylim = c(0, 320)) +
  labs(x = "",
       y = "",
       subtitle = "47 kOhm, RMS = 7.80 mV")

p3 = ggplot(Lab9Data) +
  geom_histogram(aes(x = newV94k)) +
  coord_cartesian(xlim = c(-0.03, 0.03), ylim = c(0, 320)) +
  labs(x = "",
       y = "",
       subtitle = "94 kOhm, RMS = 7.75 mV")

p4 = ggplot(Lab9Data) +
  geom_histogram(aes(x = newV220k)) +
  coord_cartesian(xlim = c(-0.03, 0.03), ylim = c(0, 320)) +
  labs(x = "",
       y = "Counts",
       subtitle = "220 kOhm, RMS = 6.87 mV")

p5 = ggplot(Lab9Data) +
  geom_histogram(aes(x = newV672k)) +
  coord_cartesian(xlim = c(-0.03, 0.03), ylim = c(0, 320)) +
  labs(x = "Residual Voltage (Volts)",
       y = "",
       subtitle = "672 kOhm, RMS = 6.80 mV")

p1 + p2 + p3 + p4  + p5  +
  plot_annotation(title = "Johnson Noise Histograms") & 
  theme(plot.title = element_text(size = rel(1.5))) 