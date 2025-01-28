const fs = require("fs");
const readline = require("readline");

class Student {
    constructor(name, age, grade) {
        this.name = name;
        this.age = age;
        this.grade = grade;
        this.id = this.generateRandomID();
    }

    // Method to generate random 8-character alphanumeric ID
    generateRandomID() {
        return Math.random().toString(36).substring(2, 10).toUpperCase();
    }

    // Method to check if the student's age is within the valid range
    isAgeValid() {
        if (this.grade === 10) {
            return this.age >= 14 && this.age <= 16;
        } else if (this.grade === 12) {
            return this.age >= 16 && this.age <= 18;
        }
        return false;
    }
}

class RegistrationSystem {
    constructor() {
        this.grade10File = "grade10_students.json";
        this.grade12File = "grade12_students.json";
        this.initializeFiles();
    }

    // Method to initialize JSON files if they don't exist
    initializeFiles() {
        if (!fs.existsSync(this.grade10File)) {
            fs.writeFileSync(this.grade10File, JSON.stringify([]));
        }
        if (!fs.existsSync(this.grade12File)) {
            fs.writeFileSync(this.grade12File, JSON.stringify([]));
        }
    }

    // Method to load students from the file
    loadStudents(grade) {
        const file = grade === 10 ? this.grade10File : this.grade12File;
        return JSON.parse(fs.readFileSync(file, "utf8"));
    }

    // Method to save students to the file
    saveStudents(grade, students) {
        const file = grade === 10 ? this.grade10File : this.grade12File;
        fs.writeFileSync(file, JSON.stringify(students, null, 2));
    }

    // Method to register a student
    registerStudent(name, age, grade) {
        if (![10, 12].includes(grade)) {
            console.log("Error: Only grades 10 and 12 are allowed.");
            return;
        }

        const newStudent = new Student(name, age, grade);
        if (!newStudent.isAgeValid()) {
            console.log(
                `Error: Age ${age} is not valid for grade ${grade}.`
            );
            return;
        }

        const students = this.loadStudents(grade);
        students.push(newStudent);
        this.saveStudents(grade, students);

        console.log(
            `Student ${name} (ID: ${newStudent.id}) registered successfully in grade ${grade}.`
        );
    }

    // Method to display all registered students
    displayStudents(grade) {
        if (![10, 12].includes(grade)) {
            console.log("Error: Only grades 10 and 12 are allowed.");
            return;
        }

        const students = this.loadStudents(grade);
        if (students.length === 0) {
            console.log(`No students registered in grade ${grade}.`);
            return;
        }

        console.log(`Registered Students in Grade ${grade}:`);
        students.forEach((student, index) => {
            console.log(
                `${index + 1}. Name: ${student.name}, Age: ${student.age}, Grade: ${student.grade}, ID: ${student.id}`
            );
        });
    }
}

// Initialize the registration system
const system = new RegistrationSystem();

// Setup readline for custom input
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

function askQuestion(query) {
    return new Promise((resolve) => rl.question(query, resolve));
}

// Custom input loop
async function main() {
    console.log("Welcome to the Student Registration System!");
    while (true) {
        console.log("\nMenu:");
        console.log("1. Register a new student");
        console.log("2. Display students of grade 10");
        console.log("3. Display students of grade 12");
        console.log("4. Exit");

        const choice = await askQuestion("Enter your choice: ");

        switch (choice.trim()) {
            case "1": {
                const name = await askQuestion("Enter student's name: ");
                const age = parseInt(await askQuestion("Enter student's age: "), 10);
                const grade = parseInt(
                    await askQuestion("Enter student's grade (10 or 12): "),
                    10
                );

                system.registerStudent(name, age, grade);
                break;
            }
            case "2": {
                system.displayStudents(10);
                break;
            }
            case "3": {
                system.displayStudents(12);
                break;
            }
            case "4": {
                console.log("Exiting the system. Goodbye!");
                rl.close();
                return;
            }
            default: {
                console.log("Invalid choice. Please try again.");
            }
        }
    }
}

// Start the custom input loop
main();