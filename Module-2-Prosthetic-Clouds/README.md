# Prosthetic Clouds

**RC15 Pervasive Urbanism · Skills Module 2 · 2026/27**

[Programme schedule](../README.md#dates) · [Course overview](../README.md#skills-module-2-prosthetic-clouds)

## Module aim

How can a wearable device change the way we perceive, measure and interact with the city?

**Prosthetic Clouds** introduces physical computing as a method of urban investigation and spatial experimentation. Students learn to program microcontrollers, connect sensors and develop small interactive systems that operate beyond the computer screen. The body becomes a site of measurement and interaction, while the device acts as a **prosthetic interface** between its wearer and the surrounding environment.

Unlike approaches that analyse existing online datasets, this module explores how we can **produce our own observations** through situated sensing. A measurement is never neutral: what we choose to sense, where we collect it, how frequently we record it and how we interpret it all shape the resulting account of urban space. We will therefore consider both the technical construction of a device and the questions it makes possible.

The workshops use the **Arduino Uno R4 WiFi** as a common platform. We begin with programming fundamentals, build a modular sensor-based data logger, and then use AI-assisted coding to experiment with programmable light and extend an existing system. The intention is not to produce a finished commercial product, but to develop the ability to conceive, construct, test and critically evaluate an interactive prototype.

## Key learning outcomes

By the end of the module, students should be able to:

1. **Understand physical computing.** Explain how microcontrollers connect inputs, computation and outputs, and identify appropriate applications for sensing and interaction.
2. **Read and modify Arduino programs.** Work with the basic structures of Arduino C/C++, including variables, conditions, loops, functions and libraries; compile, upload and debug sketches.
3. **Connect and integrate electronic components.** Understand the roles of analogue sensing and digital communication, including UART and SPI, and test hardware modules independently before combining them.
4. **Collect and document situated data.** Combine sensor readings with GPS location and time, save structured records to CSV, and recognise limitations such as calibration, missing readings and unreliable positioning.
5. **Design responsive behaviour.** Use LEDs and the Uno R4 WiFi's built-in matrix to explore rhythm, movement, visual states and communication between a device and its user.
6. **Use AI critically in programming.** Translate an intention into a technical specification, evaluate generated code, troubleshoot errors and verify behaviour on physical hardware. Understand the roles of Arduino CLI, tool calling and MCP in more automated workflows.
7. **Develop and communicate a prototype.** Make informed decisions about component organisation, portability and bodily use, and explain the relationship between a design question, its technical implementation and the observations it produces.

## Workshop sequence

### 01 — Introduction to Arduino and Programming

**6 November 2026 · 14:00–18:00**

We introduce the Arduino ecosystem and the Uno R4 WiFi, beginning with a simple LED program. Through short exercises, students learn the fundamentals of Arduino C/C++ and the sequence of writing, compiling, uploading and testing a sketch. The emphasis is on understanding how a program works rather than copying code without explanation.

**Outcome:** A series of working sketches that demonstrate basic programming concepts.

[Open Day 1 tutorial](Skills%202%20-%20Day%201%20Arduino%20Coding/README.md)

### 02 — Sensors and Actuators: Building a Modular Data Logger

**20 November 2026 · 14:00–18:00**

We move from programming to physical measurement. Students connect and test a galvanic skin response (GSR) sensor, a GPS receiver and an SD card module. Each component is introduced separately before the hardware and code are integrated into a portable logger. We examine analogue readings, serial communication, structured CSV files and the importance of testing each part of a system.

**Outcome:** A working prototype that records sensor measurements alongside location and time.

[Open Day 2 tutorial](Skills%202%20-%20Day%202%20Sensors%20and%20Actuators/README.md)

### 03 — AI-Assisted Arduino Programming

**11 December 2026 · 14:00–18:00**

The final session explores AI as a collaborator in technical and creative experimentation. Students design animated behaviours for the Uno R4 WiFi's built-in LED matrix, translate visual intentions into specifications and test AI-generated code. They then consider how to extend their existing data logger with a meaningful new behaviour. We also introduce **Arduino CLI**, showing how compilation and uploading can be performed through commands, and how connected tools and MCP can support AI-assisted development.

**Outcome:** A tested interactive behaviour or extension, accompanied by a clear account of its design intention, code and verification.

[Open Day 3 tutorial](Skills%202%20-%20Day%203%20AI-Assisted%20Arduino%20Programming/README.md)

## From technical exercises to urban investigation

The three workshops provide a foundation for designing a **wearable or portable sensing device** in response to a question about urban experience. Students should think critically about what their device measures, what it cannot measure and how its physical placement influences the observations it produces.

A successful investigation brings together **research intention, technical reliability, spatial context and design quality**. The recorded information can subsequently be analysed and represented using Python or Rhino/Grasshopper, connecting the physical experiments of Prosthetic Clouds with the data-oriented methods introduced in Cartographies of Affect. The textile workshops offer further opportunities to consider how electronic components might be integrated with the body through soft, articulated surfaces.

## Working principles

- **Build incrementally.** Start with a simple working example, then introduce one new capability at a time.
- **Test on real hardware.** A successful compilation is not proof that a device behaves as intended.
- **Document decisions.** Keep working sketches, wiring notes, sample data and records of unsuccessful as well as successful tests.
- **Interpret carefully.** Sensor values are measurements, not direct explanations of feelings or urban conditions; interpretation requires context.
- **Remain in control of AI assistance.** Use generated code as material for investigation, and be able to explain the final system.

## Resources

- [Arduino Uno R4 WiFi documentation](https://docs.arduino.cc/hardware/uno-r4-wifi/)
- [Arduino language reference](https://docs.arduino.cc/language-reference/)
- [Arduino CLI documentation](https://docs.arduino.cc/arduino-cli/)
- [RC15 software and equipment resources](../Resources.md)
