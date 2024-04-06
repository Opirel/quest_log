import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { QuestP } from './questAPI';

export interface QuestState {
  Qname: string;
  Qdescription: string;
  Qcompleted: boolean;
  Qreward: string;
  QpcInvolved: string[]; // Correctly typed as an array of strings
  status: 'idle' | 'loading' | 'failed'; // Track the loading state
}

// Ensure the initialState matches the new interface
const initialState: QuestState = {
  Qname: "",
  Qdescription: "",
  Qcompleted: false,
  Qreward: "",
  QpcInvolved:[], // Initialized as an empty array
  status: 'idle',
};

export const QuestAsync = createAsyncThunk(
  'Quest/Quest',
  async (payload: { name: string; description: string; completed: boolean; reward: string; pc_involved: string[]}) => {
    return await QuestP(payload); // Pass the whole payload directly
  }
);
export const fetchQuests = createAsyncThunk(
  'quests/fetchAll',
  async () => {
    const response = await fetch('/quests');
    const quests = await response.json();
    return quests;
  }
);

export const questSlice = createSlice({
  name: 'Quest',
  initialState,
  reducers: {
    // Define any synchronous reducers/actions here, if necessary
  },
  extraReducers: (builder) => {
    builder
      .addCase(QuestAsync.pending, (state) => {
        state.status = 'loading';
      })
      .addCase(QuestAsync.fulfilled, (state, action) => {
        const { Qname, Qdescription, QpcInvolved, Qcompleted, Qreward } = action.payload;
        state.Qname = Qname;
        state.Qdescription = Qdescription;
        // Ensure QpcInvolved is treated as an array
        state.QpcInvolved = QpcInvolved;
        state.Qcompleted = Qcompleted;
        state.Qreward = Qreward;
        state.status = 'idle';
      })
      .addCase(QuestAsync.rejected, (state) => {
        state.status = 'failed';
      });
  },
});

// export const fetchQuestsSlice = createSlice({
//   name: 'quests',
//   initialState,
//   reducers: {
//     // Define any synchronous reducers/actions here, if necessary
//   },
//     extraReducers: (builder) => {
//       builder
//         // Handle other cases like QuestAsync
//         .addCase(fetchQuests.pending, (state) => {
//           state.status = 'loading';
//         })
//         .addCase(fetchQuests.fulfilled, (state, action) => {
//           // Assuming you want to store fetched quests in an array
//           state.quests = action.payload;
//           state.status = 'idle';
//         })
//         .addCase(fetchQuests.rejected, (state) => {
//           state.status = 'failed';
//         });
//     }
//   })


export default questSlice.reducer;
