// A mock function to mimic making an async request for data
import axios from 'axios'
const MY_SERVER= 'http://127.0.0.1:8000/quests'
// API Function with adjusted parameter structure
export const QuestP = async (payload: { quest_name: string, description: string, completed: boolean, reward: string, pc_involved: string[] }) => {
  const response = await axios.post(MY_SERVER, payload);
  console.log('API request successful');
  return response.data; // Adjust based on your server response
}

