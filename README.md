# Nightlight

This is a small script for an RP2040 board (Raspberry Pi Pico... Tiny2040...) to be used with a light dependent resistor and lighting of your choice. The RP2040's PWM capabilities are used to read the light level and once it falls below a certain level start a series of loops to smoothly fade in and out the light.

Pay attention to how much current your chosen lights require, if they will draw a lot of current you may want to use a buffer circuit of some kind.
