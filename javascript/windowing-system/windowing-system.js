// @ts-check

/**
 * Implement the classes etc. that are needed to solve the
 * exercise in this file. Do not forget to export the entities
 * you defined so they are available for the tests.
 */


export function Size(width = 80, height = 60) {
    this.width = width;
    this.height = height;
}

Size.prototype.resize = function (newWidth, newHeight) {
    this.width = newWidth;
    this.height = newHeight;
}

export function Position(x = 0, y = 0) {
    this.x = x;
    this.y = y;
}

Position.prototype.move = function (newX, newY) {
    this.x = newX;
    this.y = newY;
}

export class ProgramWindow {
    constructor() {
        this.screenSize = new Size(800, 600);
        this.size = new Size();
        this.position = new Position();
    }

    resize(newSize) {
        let desiredWidth = newSize.width;
        let desiredHeight = newSize.height;
        let maxWidth = this.screenSize.width - this.position.x;
        let maxHeight = this.screenSize.height - this.position.y;

        if (newSize.width < 1) {
            desiredWidth = 1;
        } else if (newSize.width > maxWidth) {
            desiredWidth = maxWidth;
        }

        if (newSize.height < 1) {
            desiredHeight = 1;
        } else if (newSize.height > maxHeight) {
            desiredHeight = maxHeight;
        }

        this.size.resize(desiredWidth, desiredHeight);
    }

    move(position) {
        let desiredX = position.x;
        let desiredY = position.y;

        let maxX = this.screenSize.width - this.size.width;
        let maxY = this.screenSize.height - this.size.height;

        if (position.x < 0) {
            desiredX = 0;
        } else if (position.x > maxX) {
            desiredX = maxX;
        }

        if (position.y < 0) {
            desiredY = 0;
        } else if (position.y > maxY) {
            desiredY = maxY;
        }

        this.position.move(desiredX, desiredY);
    }

}

export function changeWindow(programWindow) {
    let newSize = new Size(400,300);
    programWindow.resize(newSize);

    let newPosition = new Position(100,150);
    programWindow.move(newPosition);

    return programWindow;
}
