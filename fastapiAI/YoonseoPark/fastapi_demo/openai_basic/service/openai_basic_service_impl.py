from openai_basic.repository.openai_basic_repository_impl import OpenAIBasicRepositoryImpl
from openai_basic.service.openai_basic_service import OpenAIBasicService

class OpenAIBasicServiceImpl(OpenAIBasicService):
    def __init__(self):
        self.openAIBasicRepository = OpenAIBasicRepositoryImpl()

    async def letsTalk(self, userSendMessage):
        return await self.openAIBasicRepository.generateText(userSendMessage)