# Use an official Node.js image as the base
FROM node:20

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json (if exists) first for caching
COPY package.json package-lock.json* ./

# Install dependencies
RUN npm install

# Copy the rest of the frontend code
COPY . .

# Expose the Vite development server port
EXPOSE 5173

# Start the Vite dev server
CMD ["npm", "run", "dev", "--", "--host"]
